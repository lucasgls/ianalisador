import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from dotenv import load_dotenv

load_dotenv()

class AzureAIService:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_ENDPOINT")
        self.key = os.getenv("AZURE_KEY")
        
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