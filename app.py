import streamlit as st

from agents.chatbot import ChatBotAgent
from services.whisper_service import WhisperService
from services.tts_service import TTSService
from services.conversation_manager import ConversationManager

from ui.sidebar import show_sidebar
from ui.chat_window import show_chat_history


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Voice Bot",
    page_icon="🎤",
    layout="centered"
)


# ============================================================
# TITLE
# ============================================================

st.title("🎤 AI Voice Bot")

st.write(
    "Speak to the AI and get a spoken response."
)


# ============================================================
# SIDEBAR
# ============================================================

show_sidebar()


# ============================================================
# INITIALIZE SERVICES
# ============================================================

if "chatbot" not in st.session_state:

    st.session_state.chatbot = ChatBotAgent()


if "whisper" not in st.session_state:

    st.session_state.whisper = WhisperService()


if "conversation" not in st.session_state:

    st.session_state.conversation = (
        ConversationManager()
    )


# ============================================================
# CLEAR CONVERSATION BUTTON
# ============================================================

if st.sidebar.button("🗑️ Clear Conversation"):

    st.session_state.conversation.clear()

    st.rerun()


# ============================================================
# DISPLAY OLD CHAT
# ============================================================

show_chat_history(
    st.session_state.conversation.get_messages()
)


# ============================================================
# VOICE INPUT
# ============================================================

st.subheader("🎤 Speak")

audio = st.audio_input(
    "Record your question"
)


# ============================================================
# PROCESS VOICE
# ============================================================

if audio is not None:

    # --------------------------------------------------------
    # SPEECH TO TEXT
    # --------------------------------------------------------

    with st.spinner("🎧 Understanding your voice..."):

        question = (
            st.session_state.whisper
            .transcribe(audio)
        )

    # --------------------------------------------------------
    # MAKE SURE QUESTION IS STRING
    # --------------------------------------------------------

    if question is not None:

        question = str(question).strip()

    # --------------------------------------------------------
    # CHECK QUESTION
    # --------------------------------------------------------

    if question:

        st.write("### 🗣️ You said:")

        st.write(question)

        # ----------------------------------------------------
        # GET PREVIOUS CONVERSATION
        # ----------------------------------------------------

        previous_messages = (
            st.session_state.conversation
            .get_messages()
            .copy()
        )

        # ----------------------------------------------------
        # ASK AI
        # ----------------------------------------------------

        with st.spinner("🤖 Thinking..."):

            answer = (
                st.session_state.chatbot.ask(
                    previous_messages,
                    question
                )
            )

        # ----------------------------------------------------
        # MAKE ANSWER STRING
        # ----------------------------------------------------

        if answer is None:

            answer = ""

        answer = str(answer).strip()

        # ----------------------------------------------------
        # SAVE USER MESSAGE
        # ----------------------------------------------------

        st.session_state.conversation.add_user_message(
            question
        )

        # ----------------------------------------------------
        # SAVE AI MESSAGE
        # ----------------------------------------------------

        st.session_state.conversation.add_assistant_message(
            answer
        )

        # ----------------------------------------------------
        # DISPLAY ANSWER
        # ----------------------------------------------------

        st.write("### 🤖 Bot:")

        st.write(answer)

        # ----------------------------------------------------
        # TEXT TO SPEECH
        # ----------------------------------------------------

        if answer:

            with st.spinner("🔊 Speaking..."):

                tts = TTSService()

                tts.speak(answer)