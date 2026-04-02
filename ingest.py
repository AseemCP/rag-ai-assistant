from langchain_community.document_loaders import PyPDFium2Loader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = PyPDFium2Loader(
    file_path="temp.pdf",
    mode="single",
    pages_delimiter=""
)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

splitted_text = text_splitter.split_documents(documents=docs)

embeddings = HuggingFaceEmbeddings(model="BAAI/bge-small-en")

vector_store = FAISS.from_documents(
    documents=splitted_text,
    embedding=embeddings
)