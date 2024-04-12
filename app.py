import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# We are using open source llm for now
os.environ['OPENAI_API_KEY']="USE_YOUR_API_KEY"
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_API_KEY']="ls__167978455811441d9b3ef86b11524f8e"

# Prompt Templete
prompt=ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Please response to the queries'),
        ('user',"Question:{question}")
    ]
)

llm_gpt=ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.8
)

llm_groq=ChatGroq(
    api_key="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",
    model='mixtral-8x7b-32768'
)

output_parser=StrOutputParser()

chain_gpt = prompt | llm_gpt | output_parser
chain_groq = prompt | llm_groq | output_parser

st.title("Open AI chatbot!!")
input_text=st.text_input("Ask what you want...")

if input_text:
    st.write(chain_groq.invoke({'question':input_text}))
