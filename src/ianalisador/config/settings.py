import os
from typing import List

APP_NAME = "Analisador de Currículos IA"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Sistema inteligente para análise de compatibilidade entre currículos e vagas"

PAGE_CONFIG = {
    "page_title": IAnalisador,
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

ALLOWED_FILE_TYPES = ["pdf"]
MAX_FILE_SIZE_MB = 10

AI_CONFIG = {
    "provider": "openai",  
    "model": "gpt-3.5-turbo",
    "max_tokens": 1000,
}

JOBS_FILE_PATH = "src/ianalisador/utils/jobs.json"