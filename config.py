import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#api_key = st.secrets["openai"]["api_key"]
os.environ["OPENAI_API_KEY"] = st.secrets["openai"]["api_key"]

MODEL_NAME = "gpt-4o-mini"
