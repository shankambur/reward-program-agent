from langchain_openai import ChatOpenAI


def generate_answer(question, docs,temperature):
    context = "\n\n".join([doc.page_content for (doc,score) in docs])
        # If the answer is not in the context, say:
        # "I could not find the answer in the uploaded PDFs."   

    prompt = f"""
        You are a helpful AI assistant.

        Answer the question using ONLY the context below.
        Use the context below primarily.
        You may add simple real-world examples if helpful.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    print("**** Calling API to get appropriate answer ***")
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature
    )

    response = llm.invoke(prompt)

    return response.content