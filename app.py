from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq


def rag_model(query):
    from retriever import retreive
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    query = query#"Why Use ER Diagrams In DBMS?"
    retreive = retreive
    relevant_docs = retreive.invoke(query)

    context = "\n".join(doc.page_content for doc in relevant_docs)

    prompt = f"""You are an AI assistant that answers questions using the provided context.
    If the answer is not in the context, say "I don't know."
    convert into exam ready points in exam point of view

    Context : {context}
    Question : {query}
    )
    """
    response = llm.invoke(prompt)
    return response