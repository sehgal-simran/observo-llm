import logging
import os

# Default configuration settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "llm_observability.log")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_config():
    """Return the configuration settings as a dictionary."""
    return {
        "log_level": LOG_LEVEL,
        "log_file": LOG_FILE,
        "openai_api_key": OPENAI_API_KEY,
    }
