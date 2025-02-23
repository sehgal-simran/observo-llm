# Observo LLM

LLM Observability is a Python library designed for logging, monitoring, and performance tracking of large language models (LLMs). It provides decorators and utilities to ensure model reliability, optimize inference latency, and maintain detailed logs for debugging and analysis.

## Features
- **Logging**: Captures and stores logs for LLM interactions.
- **Monitoring**: Tracks API usage, error rates, and response times.
- **Performance Tracking**: Measures inference latency and system resource utilization.
- **Tracing**: Enables tracing of requests to identify bottlenecks.

## Installation
```sh
pip install llm-observability
```

## Usage
```python
from observo_llm import monitor, trace

@monitor
@trace
def query_llm(prompt):
    # Call your LLM API here
    return "Generated response"

response = query_llm("What is AI?")
```

## Configuration
Set up environment variables for OpenAI or other API keys:
```sh
export OPENAI_API_KEY="your-api-key"
```
