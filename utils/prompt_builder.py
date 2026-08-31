def build_prompt(context, question):

    system_prompt = """
You are a helpful AI voice assistant.

Answer the user's questions clearly and naturally.

Use previous conversation when it is useful.

You are not restricted to a knowledge base.

If there is no additional context, answer using your general knowledge.

Keep your answers reasonably short because this is a voice assistant.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt.strip()
        }
    ]

    # -----------------------------------------
    # Add previous conversation
    # -----------------------------------------

    if context:

        for message in context:

            # Make sure message is a dictionary
            if not isinstance(message, dict):
                continue

            role = message.get("role")
            content = message.get("content")

            # Only accept valid roles
            if role not in ["user", "assistant"]:
                continue

            # Ignore empty content
            if content is None:
                continue

            # Convert content to string
            content = str(content).strip()

            if not content:
                continue

            messages.append({
                "role": role,
                "content": content
            })

    # -----------------------------------------
    # Add current question
    # -----------------------------------------

    question = str(question).strip()

    messages.append({
        "role": "user",
        "content": question
    })

    return messages