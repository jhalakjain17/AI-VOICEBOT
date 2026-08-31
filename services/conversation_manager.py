'''this is heart of entire system
this class file works on the basis of Orchestrator

example of  patterns:
 1.ReAct: reasoning and action
 2.Sequential pattern
 3.hierarchical
 4.Orechestrator Patterns
 5.supervised agent
 
 
 adopted pattern:Orchestrator Pattern
 it will cordinate entire flow
 
 1. LLM.wiki
2.skill.md '''

class ConversationManager:

    def __init__(self):

        self.messages = []

    def add_user_message(self, message):

        if message is None:
            return

        message = str(message).strip()

        if message == "":
            return

        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_assistant_message(self, message):

        if message is None:
            return

        message = str(message).strip()

        if message == "":
            return

        self.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_messages(self):

        return self.messages

    def clear(self):

        self.messages = []