import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Analisador de Currículos IA"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Sistema inteligente para análise de compatibilidade entre currículos e vagas"

PAGE_CONFIG = {
    "page_title": "IAnalisador",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

ALLOWED_FILE_TYPES = ["pdf"]
MAX_FILE_SIZE_MB = 10
JOBS_FILE_PATH = "src/ianalisador/utils/jobs.json"

AZURE_CONFIG = {
    "endpoint": os.getenv("AZURE_COGNIZER_ENDPOINT"),
    "key": os.getenv("AZURE_COGNIZER_KEY"),
}

OPENAI_CONFIG = {
    "endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "key": os.getenv("OPENAI_API_KEY"),
    "max_tokens": 1000,
}