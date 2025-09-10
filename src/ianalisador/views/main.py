import streamlit as st

from src.ianalisador.utils.jobs_database import JobsDatabase

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
            JobsDatabase().get_jobs_title(),
            help="Selecione a vaga para comparar com o currículo enviado"
        )
        st.divider()
        
        st.subheader("🚀 Análise Inteligente")
        st.write("• Compare seu currículo com vagas reais")
        st.write("• Receba feedback instantâneo da IA")
        st.write("• Descubra suas chances de contratação")
    
    st.title("Analisador de Currículos IA ")
    
    with st.container(border=True):
        st.subheader(f"📋 Vaga: {chart_selection}")

        vaga = JobsDatabase().get_job_by_title(chart_selection)

        if vaga:
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col1:
                st.metric("**🔢 ID da Vaga:**", f"#{vaga['id']}")
            
            with col2:
                st.write("**📝 Descrição da Vaga:**")
                st.write(vaga["descricao"])
                st.write("**⏰ Experiência Necessária:**")
                st.write(vaga["tempo_experiencia"])
                
            with col3:            
                st.write("**🛠️ Habilidades Requeridas:**")
                for habilidade in vaga["habilidades_requeridas"]:
                    st.write(f"- {habilidade}")
        else:
            st.error("❌ Vaga não encontrada!") 
    
    uploaded_files = st.file_uploader(
        "📄 Faça upload dos currículos (PDF)",
        type="pdf",
        help="Selecione um ou mais arquivos PDF com os currículos para análise",
        accept_multiple_files=True
    )