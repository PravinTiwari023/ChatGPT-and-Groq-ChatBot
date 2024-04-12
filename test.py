import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY']=os.getenv('OPEN_AI_API_KEY')

llm_groq=ChatGroq(
    api_key=os.getenv('GROQ_API_KEY'),
    model='mixtral-8x7b-32768'
)

llm_gpt=ChatOpenAI(
    temperature=0.8
)

print(llm_groq.invoke("hii there!!").content)
print(llm_gpt.invoke("hii there!!").content)