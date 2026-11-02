from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text="""
Hi my name is Nitish
i am 35 year old

i live in gurgaon
How are you
"""


splitter=RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(chunks)