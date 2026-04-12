import os
import asyncio
import json
import requests
from openai import OpenAI

# Environment configuration
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = "http://localhost:7860" 

# THE FIX: Initialize without passing global environment proxies that cause the crash
client = OpenAI(
    base_url=API_BASE_URL, 
    api_key=API_KEY,
    http_client=None # Forces the library to use its own clean client
)
