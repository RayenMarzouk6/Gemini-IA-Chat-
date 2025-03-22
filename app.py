import streamlit as st
from chatbot import get_gemini_response

# Configuration de la page
st.set_page_config(page_title="Chatbot Gemini", page_icon="🤖")

st.title("🤖 Chatbot avec Gemini AI")
st.write("Pose une question et Gemini te répondra !")

# Stocker l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Zone d'entrée utilisateur
user_input = st.chat_input("Tape ton message ici...")
if user_input:
    # Ajouter le message de l'utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Obtenir la réponse de Gemini
    response = get_gemini_response(user_input)

    # Ajouter la réponse du bot à l'historique
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Afficher la réponse
    with st.chat_message("assistant"):
        st.write(response)
