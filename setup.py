from setuptools import setup, find_packages

setup(
    name="observo_llm",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A library for LLM observability, monitoring, logging, and performance tracking.",
    long_description=open("README.md").read(),
    url="https://github.com/sehgal-simran/observo-llm",
    packages=find_packages(),
    install_requires=[
        "openai",
        "requests"
    ],
    python_requires='>=3.6',
)