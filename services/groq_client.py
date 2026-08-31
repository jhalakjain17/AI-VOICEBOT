from groq import Groq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    MAX_TOKEN_ALLOWED,
    MODEL_TEMPERATURE
)


class GroqService:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def create_response(self, question, conversation_text=""):

        # Force everything to become a normal string
        question = str(question).strip()
        conversation_text = str(conversation_text).strip()

        system_message = """
You are a helpful AI voice assistant.

Answer the user's question clearly and naturally.

Use the previous conversation when it is useful.

You can answer general questions using your own knowledge.

Keep your answer reasonably short because this is a voice assistant.
""".strip()

        # Create messages manually.
        # Every content value here is guaranteed to be a STRING.
        messages = [
            {
                "role": "system",
                "content": system_message
            }
        ]

        if conversation_text:
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Here is the previous conversation:\n\n"
                        + conversation_text
                    )
                }
            )

        messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        # Debug information
        print("\n========== GROQ REQUEST ==========")

        for i, message in enumerate(messages):

            print(
                f"Message {i}: "
                f"role={message['role']!r}, "
                f"content_type={type(message['content']).__name__}, "
                f"content={message['content']!r}"
            )

        print("==================================\n")

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=MODEL_TEMPERATURE,
            max_completion_tokens=MAX_TOKEN_ALLOWED
        )

        return response.choices[0].message.content