import psutil
import logging

def log_cpu_usage():
    """Logs the current CPU usage percentage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f"CPU Usage: {cpu_usage}%")

def log_memory_usage():
    """Logs the current memory usage details."""
    memory_info = psutil.virtual_memory()
    logging.info(f"Memory Usage: {memory_info.percent}% - Available: {memory_info.available / (1024**2):.2f} MB")

def log_disk_usage():
    """Logs the current disk usage details."""
    disk_info = psutil.disk_usage('/')
    logging.info(f"Disk Usage: {disk_info.percent}% - Free: {disk_info.free / (1024**3):.2f} GB")

def log_system_performance():
    """Logs overall system performance metrics."""
    log_cpu_usage()
    log_memory_usage()
    log_disk_usage()