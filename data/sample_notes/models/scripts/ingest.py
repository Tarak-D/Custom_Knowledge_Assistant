import os
from langchain.document_loaders import TextLoader, PyMuPDFLoader, NotionDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

loaders = [
    TextLoader("data/sample_notes/", glob="*.md"),
    PyMuPDFLoader("data/sample_notes/"),
    NotionDirectoryLoader("data/sample_notes/")
]

documents = []
for loader in loaders:
    try:
        documents.extend(loader.load())
    except Exception as e:
        print(f"Skipping loader due to error: {e}")

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("models/vector_store")
