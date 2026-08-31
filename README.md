AI Voice Bot

An **AI-powered Voice Bot** that allows users to communicate with an AI assistant using their voice. The application converts speech into text, processes the text using an LLM, and converts the AI response back into speech.

## 🚀 Features

🎤 **Voice Input** – Speak naturally through your microphone.
📝 **Speech-to-Text** – Converts voice into text using Whisper.
🧠 **AI Conversation** – Generates intelligent responses using a Large Language Model.
🔊 **Text-to-Speech** – Converts AI responses into natural-sounding speech.
💬 **Conversation History** – Maintains the context of the conversation.
🖥️ **Streamlit Interface** – Simple and interactive web interface.
⚡ **Fast AI Responses** – Uses Groq API for fast inference.

## ⚙️ How It Works

```text
🎤 User Voice
      ↓
Whisper Speech-to-Text
      ↓
📝 Text
      ↓
Groq LLM
      ↓
🤖 AI Response
      ↓
Text-to-Speech
      ↓
🔊 Voice Response
```


Create a Virtual Environment:-

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=your_model_name
MODEL_TEMPERATURE=0.7
MAX_TOKEN_ALLOWED=1024
EMBEDDING_MODEL=your_embedding_model
```

> ⚠️ Never upload your `.env` file or API key to GitHub.


## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example

**User:**

> "What is machine learning?"

**AI Voice Bot:**

> "Machine learning is a branch of artificial intelligence that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed."

The response is then converted into speech and played to the user.

## 🎯 Use Cases

* Personal AI assistant
* Voice-based learning assistant
* Customer support chatbot
* Interactive AI applications
* Voice-controlled applications
* Educational assistants

## 🔮 Future Improvements

* 🌍 Support for multiple languages
* 👤 User authentication
* 🗃️ Persistent conversation history
* 🎙️ Better voice recognition
* 😊 Emotion-aware responses
* ☁️ Cloud deployment
* 📱 Mobile-friendly interface

