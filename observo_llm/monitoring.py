import time
import logging

def track_execution_time(func):
    """Decorator to track execution time of functions."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

def record_metrics(metric_name, value):
    """Logs a metric with a specific value."""
    logging.info(f"METRIC - {metric_name}: {value}")

def track_api_call(api_name, response_time, success=True):
    """Logs API call metrics including response time and success status."""
    status = "SUCCESS" if success else "FAILURE"
    logging.info(f"API_CALL - {api_name}: {response_time:.4f}s, Status: {status}")
