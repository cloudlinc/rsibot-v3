-- Bot health monitoring table
create table bot_health (
    bot_id text not null,
    broker_type text not null,
    status text not null,
    details jsonb not null default '{}',
    hostname text not null,
    last_seen timestamp with time zone not null,
    primary key (bot_id)
);

-- Error logging table
create table bot_errors (
    id uuid default uuid_generate_v4() primary key,
    bot_id text not null,
    broker_type text not null,
    error_type text not null,
    error_message text not null,
    stack_trace text,
    context jsonb not null default '{}',
    hostname text not null,
    created_at timestamp with time zone not null,
    resolved_at timestamp with time zone
);

-- Trade attempts tracking
create table trade_attempts (
    id uuid default uuid_generate_v4() primary key,
    bot_id text not null,
    broker_type text not null,
    trade_type text not null,
    ticker text not null,
    success boolean not null,
    details jsonb not null default '{}',
    hostname text not null,
    created_at timestamp with time zone not null
);

-- Create indexes for better query performance
create index bot_health_last_seen_idx on bot_health(last_seen);
create index bot_errors_created_at_idx on bot_errors(created_at);
create index trade_attempts_created_at_idx on trade_attempts(created_at);

-- Create a view for active bots (seen in last 10 minutes)
create view active_bots as
select *
from bot_health
where last_seen > now() - interval '10 minutes';

-- Create a view for recent errors
create view recent_errors as
select *
from bot_errors
where created_at > now() - interval '24 hours'
order by created_at desc; 