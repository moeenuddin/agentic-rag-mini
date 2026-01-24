from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool
from llama_index.llms.openai import OpenAI
from ingest import build_index
from config import MODEL_NAME
import os

index = build_index()

llm = OpenAI(model=MODEL_NAME,api_key=os.environ["OPENAI_API_KEY"])

query_tool = QueryEngineTool.from_defaults(
    index.as_query_engine(similarity_top_k=3),
    name="document_search",
    description="Search course documents for relevant information"
)

agent = ReActAgent.from_tools(
    tools=[query_tool],
    llm=llm,
    system_prompt="""
You are an intelligent academic assistant.

Before answering:
1. Decide whether the document contains sufficient information.
2. If information is missing or ambiguous, ask a clarification question.
3. If sufficient, answer concisely using the document.
4. Do NOT hallucinate.
"""
)
