from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def create_vector_store(chunks):
    documents = []

    for i, chunk in enumerate(chunks, start=1):
        documents.append(
            Document(
                page_content=chunk["content"],
                metadata={
                    "source": chunk["source"],
                     "page": chunk["page"],
                      "chunk_id": i
                }
            )
        )
    print("++++++documents++++\n",documents)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    print("%%%%%%%%%%Start Embedding%%%%%%%%%%%%%")
    vector_store = FAISS.from_documents(documents, embeddings)
    print("%%%%%%%%%%Completed Embedding%%%%%%%%%")

    return vector_store


def save_vector_store(vector_store):

    vector_store.save_local("vectorstore")


def load_vector_store():

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )