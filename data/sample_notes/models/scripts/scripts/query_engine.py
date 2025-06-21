from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

embedding = OpenAIEmbeddings()
vectorstore = FAISS.load_local("models/vector_store", embedding)
retriever = vectorstore.as_retriever()

qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)

def ask_question(query):
    return qa.run(query)
