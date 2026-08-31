from services.groq_client import GroqService


class ChatBotAgent:

    def __init__(self):

        self.groq = GroqService()

    def ask(self, context, question):

        # Convert conversation history into plain text
        conversation_text = ""

        if context:

            for message in context:

                if not isinstance(message, dict):
                    continue

                role = str(
                    message.get("role", "")
                )

                content = message.get("content", "")

                content = str(content).strip()

                if not content:
                    continue

                if role == "user":

                    conversation_text += (
                        "User: "
                        + content
                        + "\n"
                    )

                elif role == "assistant":

                    conversation_text += (
                        "Assistant: "
                        + content
                        + "\n"
                    )

        # Make sure question is a string
        question = str(question).strip()

        # Send only strings to Groq
        response = self.groq.create_response(
            question=question,
            conversation_text=conversation_text
        )

        return response