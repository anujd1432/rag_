import os
from dotenv import load_dotenv

load_dotenv()
#loading the documents
from langchain_community.document_loaders import PyPDFLoader,TextLoader

file_path='sample_text.txt'

if file_path.endswith(".pdf"):
    loader=PyPDFLoader(file_path)
elif file_path.endswith('.txt'):
    loader=TextLoader(file_path,encoding='utf-8')

document=loader.load()
print('file load successfully')


#text splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunk=splitter.split_documents(document)
print(f"splitting is done total chunks aare {len(chunk)}")

#embadding generating
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("embedding model is ready")


#vector stores
from langchain_community.vectorstores import FAISS

vectorstores=FAISS.from_documents(chunk,embeddings)

#creaate retrievers
retriever=vectorstores.as_retriever(
    search_type='similarity',
    search_kwargs={"k":3}
)

#now finally connecting everything
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages([
    ("system","you are a helpful AI assistant ,use the context below to answer users "),
    ("human","Context : {context}, \n Question : {question}")
])

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

#chain create
chain=prompt | llm

#intraction with everything

print("rage system is ready ask any question related to document")
while True:
    question=input("your questions:-")
    if question=="":
        continue
    elif question=="quit":
        break
    retrieved_chunk=retriever.invoke(question)

    context="\n".join([doc.page_content for doc in retrieved_chunk])

    response=chain.invoke({"context":context,"question":question})
    print("answer: \n {response.content}")
