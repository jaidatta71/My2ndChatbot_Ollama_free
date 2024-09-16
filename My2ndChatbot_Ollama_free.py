#LANGCHAIN_API_KEY="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"
#LANGCHAIN_PROJECT="MySecondGIProject"
######   FREE OLLAMA Model   #####

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

## environment variables call
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## creating chatbot
## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide gentle response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With Llama2 API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=Ollama("model="llama2")
output_parser=StrOutputParser()

# chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

