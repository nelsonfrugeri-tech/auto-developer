import streamlit as st
import requests
import re

# Configuração inicial da página
st.set_page_config(page_title="Chatbot Multi-Agent", layout="centered")

# URL da API
API_URL = "http://localhost:8080/multi-agent/v1/chat"

# Inicializa a sessão de histórico da conversa
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Função para formatar respostas, destacando blocos de código
def format_response(text):
    code_blocks = re.findall(r"```(\w+)?\n(.*?)```", text, re.DOTALL)

    if code_blocks:
        for lang, code in code_blocks:
            formatted_code = f"```{lang}\n{code}\n```" if lang else f"```\n{code}\n```"
            text = text.replace(f"```{lang}\n{code}```", f"\n```{formatted_code}```\n")

    return text


# Função para enviar mensagem e obter resposta em streaming
def get_response(user_input):
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    payload = {"query": user_input}

    with requests.post(API_URL, json=payload, stream=True) as response:
        response.raise_for_status()

        # Placeholder para exibir resposta progressivamente
        message_placeholder = st.empty()
        full_response = ""

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                decoded_chunk = chunk.decode("utf-8")
                full_response += decoded_chunk
                formatted_response = format_response(full_response)
                message_placeholder.markdown(f"**🤖 Assistente:** {formatted_response}")

    st.session_state.chat_history.append(
        {"role": "assistant", "content": full_response}
    )


# Exibição do título
st.title("💬 Chatbot Multi-Agent")

# Renderiza o histórico da conversa
for message in st.session_state.chat_history:
    role = message["role"]
    content = format_response(message["content"])

    if role == "user":
        st.markdown(f"**🧑‍💻 Você:** {content}")
    elif role == "assistant":
        if "```" in content:
            st.markdown(f"**🤖 Assistente:**")
            st.code(content)
        else:
            st.markdown(f"**🤖 Assistente:** {content}")

# Campo de entrada para nova mensagem
user_input = st.text_area("Digite sua mensagem:", key="user_input", height=120)

# Botão de envio
if st.button("Enviar") and user_input.strip():
    get_response(user_input)
