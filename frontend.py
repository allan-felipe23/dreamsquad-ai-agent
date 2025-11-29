import streamlit as st
import requests
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="DreamSquad AI",
    page_icon="✨",
    layout="centered"
)

# --- URL DA API (Backend) ---
API_URL = "http://127.0.0.1:8000/chat"

# --- ESTILOS CSS PERSONALIZADOS ---
def local_css():
    st.markdown("""
    <style>
    /* 1. Fundo com Gradiente Sutil Animado */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* 2. Título em Gradiente (Texto "DreamSquad") */
    .gradient-text {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        background: -webkit-linear-gradient(45deg, #FFFFFF, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        text-align: center;
        margin-bottom: 0px;
    }

    /* 3. Subtítulo Minimalista */
    .subtitle {
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 30px;
    }

    /* 4. Estilização das Mensagens de Chat (Cartões) */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.15); /* Vidro fosco */
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Avatar do Usuário */
    [data-testid="stChatMessage"] [data-testid="user-avatar"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    /* Avatar da IA */
    [data-testid="stChatMessage"] [data-testid="assistant-avatar"] {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        color: white;
    }

    /* Input de Texto Flutuante */
    .stChatInput {
        position: fixed;
        bottom: 30px;
        z-index: 100;
    }
    
    /* Ajuste para modo claro/escuro automático nas fontes */
    p {
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- HEADER VISUAL ---
st.markdown('<div class="gradient-text">DreamSquad AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Sua inteligência criativa e matemática</div>', unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- EXIBIÇÃO DO HISTÓRICO ---
# Container para as mensagens (mantém o scroll correto)
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        # Define avatares personalizados
        avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
        
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# --- INPUT DO USUÁRIO ---
if prompt := st.chat_input("Digite sua pergunta ou cálculo..."):
    # 1. Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)

    # 2. Resposta da IA com efeito de "Digitação"
    with chat_container:
        with st.chat_message("assistant", avatar="🤖"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Placeholder de "Pensando..."
            message_placeholder.markdown("`⚡ Processando...`")
            
            try:
                # Chama a API
                response = requests.post(API_URL, json={"message": prompt})
                
                if response.status_code == 200:
                    ai_response = response.json().get("response", "Erro na resposta.")
                    
                    # Efeito de digitação (Typewriter Effect)
                    for chunk in ai_response.split():
                        full_response += chunk + " "
                        time.sleep(0.05) # Ajuste a velocidade aqui
                        message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                else:
                    message_placeholder.error(f"Erro na API: {response.status_code}")
                    full_response = "Erro de conexão."
            
            except Exception as e:
                message_placeholder.error(f"API Offline: {e}")
                full_response = f"Erro: {e}"
            
            # Salva no histórico
            st.session_state.messages.append({"role": "assistant", "content": full_response})