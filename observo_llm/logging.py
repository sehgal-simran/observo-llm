import logging
import os
from datetime import datetime

# Create logs directory if not exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, f"observo_llm{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_request(model_name, prompt):
    """Logs LLM request details."""
    logging.info(f"LLM Request - Model: {model_name}, Prompt: {prompt}")

def log_response(model_name, response):
    """Logs LLM response details."""
    logging.info(f"LLM Response - Model: {model_name}, Response: {response}")

def log_error(error_message):
    """Logs errors encountered during LLM calls."""
    logging.error(f"LLM Error - {error_message}")

if __name__ == "__main__":
    # Test logging functions
    log_request("gpt-4", "What is the capital of France?")
    log_response("gpt-4", "The capital of France is Paris.")
    log_error("Timeout occurred while fetching response from LLM.")
