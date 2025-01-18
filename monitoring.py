import logging
import os
import socket
import traceback
from datetime import datetime, timezone
from functools import wraps
from typing import Optional, Dict, Any

from supabase import create_client, Client

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BotMonitor:
    def __init__(self, supabase: Client):
        self.supabase = supabase
        self.hostname = socket.gethostname()
        self.bot_id = os.getenv('BOT_ID', self.hostname)
        self.broker_type = os.getenv('BROKER_TYPE', 'unknown')

    def record_heartbeat(self, status: str = 'healthy', details: Optional[Dict[str, Any]] = None):
        """Record a heartbeat with the current bot status"""
        try:
            data = {
                'bot_id': self.bot_id,
                'broker_type': self.broker_type,
                'status': status,
                'details': details or {},
                'hostname': self.hostname,
                'last_seen': datetime.now(timezone.utc).isoformat(),
            }
            self.supabase.table('bot_health').upsert(data).execute()
        except Exception as e:
            logger.error(f"Failed to record heartbeat: {str(e)}")

    def record_error(self, error: Exception, context: Optional[Dict[str, Any]] = None):
        """Record an error with full stack trace and context"""
        try:
            data = {
                'bot_id': self.bot_id,
                'broker_type': self.broker_type,
                'error_type': type(error).__name__,
                'error_message': str(error),
                'stack_trace': traceback.format_exc(),
                'context': context or {},
                'hostname': self.hostname,
                'created_at': datetime.now(timezone.utc).isoformat(),
            }
            self.supabase.table('bot_errors').insert(data).execute()
        except Exception as e:
            logger.error(f"Failed to record error: {str(e)}")

    def record_trade_attempt(self, trade_type: str, ticker: str, success: bool, details: Optional[Dict[str, Any]] = None):
        """Record trade attempts, both successful and failed"""
        try:
            data = {
                'bot_id': self.bot_id,
                'broker_type': self.broker_type,
                'trade_type': trade_type,
                'ticker': ticker,
                'success': success,
                'details': details or {},
                'hostname': self.hostname,
                'created_at': datetime.now(timezone.utc).isoformat(),
            }
            self.supabase.table('trade_attempts').insert(data).execute()
        except Exception as e:
            logger.error(f"Failed to record trade attempt: {str(e)}")

def monitor_task(monitor: BotMonitor):
    """Decorator for monitoring long-running tasks"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = datetime.now(timezone.utc)
            try:
                # Record start of task
                monitor.record_heartbeat('running', {
                    'task': func.__name__,
                    'started_at': start_time.isoformat()
                })
                
                # Run the task
                result = await func(*args, **kwargs)
                
                # Record successful completion
                monitor.record_heartbeat('healthy', {
                    'task': func.__name__,
                    'last_success': datetime.now(timezone.utc).isoformat()
                })
                
                return result
            except Exception as e:
                # Record error and re-raise
                monitor.record_error(e, {
                    'task': func.__name__,
                    'started_at': start_time.isoformat()
                })
                raise
        return wrapper
    return decorator 