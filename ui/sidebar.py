import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("⚙️ Voice Bot")

        st.write("AI Voice Assistant")

        st.markdown("---")

        st.write("Features")

        st.write("🎤 Voice Input")
        st.write("🧠 Groq LLM")
        st.write("🔊 Voice Output")
        st.write("💬 Conversation Memory")