import streamlit as st


def show_chat_history(messages):

    for message in messages:

        if message["role"] == "user":

            with st.chat_message("user"):
                st.write(message["content"])

        elif message["role"] == "assistant":

            with st.chat_message("assistant"):
                st.write(message["content"])