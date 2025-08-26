import streamlit as st

def run_app():
    st.set_page_config(
        page_title="Analisador de Currículos IA",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    with st.sidebar:
        st.header("🎯 Seleção de Vaga")
        
        chart_selection = st.selectbox(
            "📋 Escolha a vaga para análise:",
            ("Gerente de Vendas", "Programador Junior"),
            help="Selecione a vaga para comparar com o currículo enviado"
        )
        
        st.divider()
        
        st.subheader("💡 Como usar:")
        st.write("1. Selecione a vaga desejada")
        st.write("2. Faça upload do currículo em PDF")
        st.write("3. Aguarde a análise da IA")
    
    st.title("Analisador de Currículos IA 🤖")
    

    st.write(f"Vaga selecionada: **{chart_selection}**")
    
    uploaded_file = st.file_uploader(
        "📄 Faça upload do currículo (PDF)",
        type="pdf",
        help="Selecione um arquivo PDF com o currículo para análise"
    )
    
    if uploaded_file is not None:
        st.success("✅ Arquivo carregado com sucesso!")