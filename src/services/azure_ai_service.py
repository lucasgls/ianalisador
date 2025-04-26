import os
import json
import google.generativeai as genai
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

genai.configure(api_key="")

class AzureAIService:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_ENDPOINT")
        self.key = os.getenv("AZURE_KEY")
        self.model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

        if not self.endpoint or not self.key:
            raise ValueError("Variáveis de ambiente AZURE_ENDPOINT e AZURE_KEY não configuradas")

        self.client = DocumentAnalysisClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.key)
        )

    def extract_text_from_pdf(self, file_stream):
        try:
            poller = self.client.begin_analyze_document(
                model_id="prebuilt-document",
                document=file_stream
            )
            result = poller.result()
            return "\n".join([line.content for page in result.pages for line in page.lines])
        except Exception as e:
            raise RuntimeError(f"Erro na extração de texto: {str(e)}")

    def carregar_requisitos_vaga(self, nome_vaga):
        try:
            caminho_vagas = Path(__file__).parent.parent / 'data' / 'vagas.json'
            with open(caminho_vagas, 'r', encoding='utf-8') as file:
                vagas = json.load(file)
                return vagas.get(nome_vaga, {}).get('requisitos', [])
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar vagas: {str(e)}")

    def analisar_compatibilidade_gemini(self, texto_curriculo, requisitos_vaga):
        try:
            prompt = f"""
            Atue como um especialista em RH analisando a compatibilidade entre um currículo e os requisitos de uma vaga.

            Requisitos da vaga:
            {requisitos_vaga}

            Currículo analisado:
            {texto_curriculo[:3000]}

            Forneça:
            - Pontos fortes do candidato
            - Skills que faltam
            - Compatibilidade geral (0-100%)
            - Recomendações de melhoria

            Formato de resposta (em português):
            • Use bullets points
            • Destaque palavras-chave
            • Seja direto e técnico
            """

            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            raise RuntimeError(f"Erro na análise com Gemini: {str(e)}")
