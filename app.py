import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from src.services.azure_ai_service import AzureAIService
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()
azure_service = AzureAIService()

nomeServico = "IAnalisador 👀"

st.set_page_config(
    page_title="Analisador de Currículos",
    page_icon="👀",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.title("Vaga a ser preenchida 👇")
    chart_selection = st.selectbox(
        "Selecione a vaga que deseja Preencher",
        ("Gerente de Vendas", "Programador Junior")
    )


st.title(f"Seja bem-vindo ao {nomeServico}")
st.write("Analisarei os dados do candidato e irei mandar dados relevantes sobre ele a seguir!")


uploaded_file = st.file_uploader("Coloque aqui o currículo:", type=["pdf"], accept_multiple_files=True)


if uploaded_file:
    files = []

    for file in uploaded_file:
        file_bytes = file.read()
        files.append(file_bytes)

    # Carrega requisitos uma única vez
    requisitos_vaga = azure_service.carregar_requisitos_vaga(chart_selection)
    
    with st.spinner('Analisando compatibilidade com a vaga...'):
        for idx, file_bytes in enumerate(files, start=1):
            # Processamento do PDF
            document_analysis_client = DocumentAnalysisClient(
                endpoint=os.getenv("AZURE_ENDPOINT"),
                credential=AzureKeyCredential(os.getenv("AZURE_KEY"))
            )
            
            poller = document_analysis_client.begin_analyze_document(
                model_id="prebuilt-document",
                document=file_bytes
            )
            
            result = poller.result()
            extracted_text = azure_service.extract_text_from_pdf(file_bytes)
            
            # Exibição dos resultados
            st.subheader(f"Análise do Candidato {idx}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.text_area(f"Texto Extraído {idx}", extracted_text, height=500)
                st.markdown("**Requisitos da Vaga**")
                for req in requisitos_vaga:
                    st.write(f"- {req}")
            
            with col2:
                analise = azure_service.analisar_compatibilidade_gemini(
                    extracted_text, 
                    requisitos_vaga
                )
                st.markdown("**Análise de Compatibilidade**")
                st.markdown(analise)