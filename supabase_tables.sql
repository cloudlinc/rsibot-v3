create table bot_config (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     rsi_buy_threshold float not null default 30,
     rsi_sell_threshold float not null default 70,
     macd_enabled boolean not null default true,
     manual_mode boolean not null default false,
     shares_per_trade integer not null default 10,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
     updated_at timestamp with time zone default timezone('utc'::text, now()) not null
   );

   create table trade_signals (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     action text not null,
     rsi float not null,
     macd float not null,
     status text not null default 'PENDING',
     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
     updated_at timestamp with time zone default timezone('utc'::text, now()) not null
   );

    create table trade_history (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     action text not null,
     rsi float not null,
     macd float not null,
     executed_at timestamp with time zone default timezone('utc'::text, now()) not null
   );

   create table trade_status (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     status text not null,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null
   );
   
   create table trade_logs (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     action text not null,
     rsi float not null,
     macd float not null,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null
   );

   create table bot_health (
     id uuid default uuid_generate_v4() primary key,
     status text not null,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null
   );

   create table bot_errors (
     id uuid default uuid_generate_v4() primary key,
     error text not null,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null
   );

   create table trade_attempts (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     action text not null,
     rsi float not null,
     macd float not null,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null
   );