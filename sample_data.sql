-- Insert sample bot health data
insert into bot_health (bot_id, broker_type, status, details, hostname, last_seen) 
values 
    ('ibkr-bot-1', 'ibkr', 'running', '{"memory_usage": "128MB", "cpu_usage": "2%"}', 'trading-bot-ibkr', now()),
    ('schwab-bot-1', 'schwab', 'running', '{"memory_usage": "156MB", "cpu_usage": "3%"}', 'trading-bot-schwab', now() - interval '2 minutes');

-- Insert sample trade history data first (this feeds the todays_trading_summary view)
insert into trade_history (bot_id, broker_type, ticker, action, rsi, macd) 
values 
    ('ibkr-bot-1', 'ibkr', 'AAPL', 'BUY', 28.5, -0.02),
    ('ibkr-bot-1', 'ibkr', 'AAPL', 'SELL', 72.3, 0.03),
    ('ibkr-bot-1', 'ibkr', 'MSFT', 'BUY', 29.1, -0.01),
    ('schwab-bot-1', 'schwab', 'GOOGL', 'BUY', 27.8, -0.015),
    ('schwab-bot-1', 'schwab', 'TSLA', 'SELL', 73.2, 0.025);

-- Insert sample trade signals
insert into trade_signals (bot_id, broker_type, ticker, action, rsi, macd, status) 
values 
    ('ibkr-bot-1', 'ibkr', 'GOOGL', 'BUY', 27.8, -0.015, 'PENDING'),
    ('schwab-bot-1', 'schwab', 'TSLA', 'SELL', 73.2, 0.025, 'PENDING');

-- Insert sample errors
insert into bot_errors (bot_id, broker_type, error_type, error_message, hostname) 
values 
    ('ibkr-bot-1', 'ibkr', 'ConnectionWarning', 'Slow connection detected', 'trading-bot-ibkr'),
    ('schwab-bot-1', 'schwab', 'AuthenticationError', 'Session expired', 'trading-bot-schwab');

-- Insert sample trade attempts
insert into trade_attempts (bot_id, broker_type, trade_type, ticker, success, details, hostname) 
values 
    ('ibkr-bot-1', 'ibkr', 'BUY', 'AAPL', true, '{"price": "150.25", "quantity": 10}', 'trading-bot-ibkr'),
    ('ibkr-bot-1', 'ibkr', 'SELL', 'AAPL', true, '{"price": "155.50", "quantity": 10}', 'trading-bot-ibkr'),
    ('schwab-bot-1', 'schwab', 'BUY', 'MSFT', false, '{"error": "Insufficient funds"}', 'trading-bot-schwab'); 