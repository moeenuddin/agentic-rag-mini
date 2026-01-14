from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.storage import StorageContext
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from config import MODEL_NAME

def build_index():
    Settings.llm = OpenAI(model=MODEL_NAME)
    docs = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(docs)
    return index
