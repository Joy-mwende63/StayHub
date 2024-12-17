# debug.py
import datetime

def log_error(message):
    """Log errors with timestamp."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('error_log.txt', 'a') as file:
        file.write(f"{timestamp} - ERROR: {message}\n")
