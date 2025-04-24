import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import requests
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

nomeServico = "IAnalisador 👀"

with st.sidebar:
    st.title("Vaga a ser preenchida 👇")
    chart_selection = st.selectbox("Selecione a vaga que deseja Preencher", 
                                    ("Vendedor", "Gerente de Vendas")
                                    )

st.title(f"Seja bem vindo ao {nomeServico}");
st.write("Analisarei os dados do candidato e irei mandar dados relevantes sobre ele a seguir! ") 


uploaded_file = st.file_uploader("Coloque aqui o currículo: ", type=["pdf"])
if uploaded_file:
    image = Image.open(uploaded_file)
else:
    image = Image.open(requests.get("https://picsum.photos/200/120", stream=True).raw)

