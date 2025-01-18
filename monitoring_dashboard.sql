-- Active Bots Status View
create or replace view active_bots_status as
select 
    bot_id,
    broker_type,
    status,
    hostname,
    last_seen,
    details,
    case 
        when last_seen > now() - interval '5 minutes' then 'Online'
        when last_seen > now() - interval '15 minutes' then 'Warning'
        else 'Offline'
    end as connection_status,
    extract(epoch from (now() - last_seen))/60 as minutes_since_last_seen
from bot_health
order by last_seen desc;

-- Today's Trading Summary View
create or replace view todays_trading_summary as
select 
    ticker,
    count(*) as total_trades,
    sum(case when action = 'BUY' then 1 else 0 end) as buy_trades,
    sum(case when action = 'SELL' then 1 else 0 end) as sell_trades,
    round(avg(rsi), 2) as avg_rsi,
    round(avg(macd), 4) as avg_macd
from trade_history
where executed_at::date = current_date
group by ticker;

-- Pending Trades View
create or replace view pending_trades_view as
select 
    id,
    ticker,
    action,
    rsi,
    macd,
    created_at,
    extract(epoch from (now() - created_at))/60 as minutes_pending
from trade_signals
where status = 'PENDING'
order by created_at;

-- Recent Errors View
create or replace view recent_errors_view as
select 
    id,
    bot_id,
    broker_type,
    error_type,
    error_message,
    created_at,
    resolved_at,
    case 
        when resolved_at is null then 'Unresolved'
        else 'Resolved'
    end as status
from bot_errors
where created_at > now() - interval '24 hours'
order by created_at desc;

-- Trading Performance View
create or replace view trading_performance as
select 
    date_trunc('hour', executed_at) as hour,
    ticker,
    count(*) as trades_count,
    round(avg(rsi), 2) as avg_rsi,
    round(avg(macd), 4) as avg_macd
from trade_history
where executed_at > now() - interval '24 hours'
group by date_trunc('hour', executed_at), ticker
order by hour desc;

-- Function to mark error as resolved
create or replace function resolve_error(error_id uuid)
returns void as $$
begin
    update bot_errors
    set resolved_at = now()
    where id = error_id;
end;
$$ language plpgsql;

-- Function to get bot health status
create or replace function get_bot_health(bot_id_param text)
returns table (
    status text,
    last_seen timestamp with time zone,
    uptime_minutes numeric,
    error_count bigint,
    trade_count bigint
) as $$
begin
    return query
    select 
        bh.status,
        bh.last_seen,
        extract(epoch from (now() - bh.last_seen))/60 as uptime_minutes,
        count(distinct be.id) as error_count,
        count(distinct th.id) as trade_count
    from bot_health bh
    left join bot_errors be on be.bot_id = bh.bot_id 
        and be.created_at > now() - interval '24 hours'
    left join trade_history th on th.created_at > now() - interval '24 hours'
    where bh.bot_id = bot_id_param
    group by bh.status, bh.last_seen;
end;
$$ language plpgsql;

-- Create a notification function for critical errors
create or replace function notify_critical_error()
returns trigger as $$
begin
    -- You can extend this to send emails or webhook notifications
    insert into bot_health (bot_id, status, details, hostname, last_seen)
    values (
        NEW.bot_id,
        'error',
        jsonb_build_object(
            'error_type', NEW.error_type,
            'error_message', NEW.error_message
        ),
        NEW.hostname,
        now()
    );
    return NEW;
end;
$$ language plpgsql;

-- Create trigger for critical errors
create trigger critical_error_trigger
    after insert on bot_errors
    for each row
    when (NEW.error_type in ('ConnectionError', 'AuthenticationError', 'TradeExecutionError'))
    execute function notify_critical_error();

-- Create materialized view for historical performance (refreshed daily)
create materialized view if not exists historical_performance as
select 
    date_trunc('day', executed_at) as trade_date,
    ticker,
    count(*) as total_trades,
    round(avg(rsi), 2) as avg_rsi,
    round(avg(macd), 4) as avg_macd,
    count(case when action = 'BUY' then 1 end) as buy_count,
    count(case when action = 'SELL' then 1 end) as sell_count
from trade_history
group by date_trunc('day', executed_at), ticker
order by trade_date desc;

-- Create index on the materialized view
create index if not exists historical_performance_date_idx 
on historical_performance(trade_date);

-- Function to refresh historical performance
create or replace function refresh_historical_performance()
returns void as $$
begin
    refresh materialized view historical_performance;
end;
$$ language plpgsql;

-- Create a daily refresh for historical performance
select cron.schedule(
    'refresh_historical_performance',
    '0 0 * * *',  -- Run at midnight every day
    $$select refresh_historical_performance()$$
); 