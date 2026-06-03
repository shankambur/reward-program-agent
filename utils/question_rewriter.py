from langchain_openai import ChatOpenAI


def rewrite_question(chat_history, current_question):

    history_text = "\n".join(
        [
            f'{msg["role"]}: {msg["content"]}'
            for msg in chat_history
        ]
    )
    print("history_text=",history_text)

    prompt = f"""
        You are a helpful AI assistant.

        Rewrite the current question into a standalone question
        using the previous conversation history.

        If the question is already standalone,
        return it unchanged.

        Rules:
        1. Do not answer the question.
        2. Do not list technologies, tools, or details.
        3. Only rewrite the user's latest question.
        4. Use chat history only to resolve references like first one, second one, it, this project, that project.
        5. Return one short question only.

        Conversation History:
        {history_text}

        Current Question:
        {current_question}

        Rewritten Question:
        """
    print("**** Calling API to rewrite the question ***")
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    response = llm.invoke(prompt)

    return response.content