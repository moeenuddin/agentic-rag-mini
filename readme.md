agentic-rag-mini/
│
├── app.py
├── agent.py
├── ingest.py
├── config.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── data/
│   └── syllabus.md
│
└── .env.example


# Agentic RAG Mini

A minimal agentic Retrieval-Augmented Generation (RAG) system using:

- Streamlit
- LlamaIndex ReAct Agent
- OpenAI GPT
- Docker

## 🧠 What Makes It Agentic?

The agent decides whether:
- the document contains enough information to answer, or
- a clarification question is required before answering.

## 🚀 Run Locally

```bash
cp .env.example .env
docker build -t agentic-rag-mini .
docker run -p 8501:8501 agentic-rag-mini

