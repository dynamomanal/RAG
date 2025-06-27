import os
from langchain_openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from streamlit_extras import add_vertical_space as avs
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

load_dotenv()

st.set_page_config(page_title="RAG", layout="wide")
st.title("📄 RAG ")

with st.sidebar:
    st.title("Chat App on custom data")
    avs.add_vertical_space(5)

def main():
    st.header("Chat with PDF")
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:
        # Extract text from PDF
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        # Define embedding and store name
        embeddings = OpenAIEmbeddings()
        store_name = pdf.name[:-4]
        folder_path = f"vectorstores/{store_name}"  # store FAISS files here

        # Create the directory if it doesn't exist
        os.makedirs("vectorstores", exist_ok=True)

        # Load or create FAISS vector store
        if os.path.exists(os.path.join(folder_path, "index.faiss")):
            VectorStore = FAISS.load_local(folder_path, embeddings,allow_dangerous_deserialization=True)
            # st.success("Loaded existing FAISS index from disk.")
        else:
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            VectorStore.save_local(folder_path)
            # st.success("Created and saved FAISS index.")
            
            
            

        query = st.text_input("Ask Queries about your PDF files ")    
        st.write(query)
        
        if query:
            docs = VectorStore.similarity_search(query=query, k=3)
            llm = OpenAI(model='gpt-3.5-turbo-instruct',temperature=2)
            chain =load_qa_chain(llm=llm , chain_type ='stuff')
            response = chain.run(input_documents=docs, question=query)
            st.write(response)
        
        
   

if __name__ == '__main__':
    main()

