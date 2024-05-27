
import streamlit as st
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


st.header('Questions to AI over a Document', divider='blue')

st.text('Upload a Document (txt, pdf or docx) and ask questions to Open AI about it.')

# File uploader for user to upload a file
uploaded_file = st.file_uploader("Upload a document...", type=["txt", "pdf", "docx"])

user_prompt = st.text_area("User prompt", placeholder="Ask a question...")

if uploaded_file is not None:
    # Check the file type and read the content accordingly
    if uploaded_file.type == "text/plain":
        # Read plain text file
        file_content = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        # Read PDF file
        import PyPDF2
        reader = PyPDF2.PdfReader(uploaded_file)
        file_content = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            file_content += page.extract_text()
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Read DOCX file
        from docx import Document
        doc = Document(uploaded_file)
        file_content = "\n".join([para.text for para in doc.paragraphs])
    else:
        st.error("Unsupported file type")

    if file_content:
        # Always display the button but disable it if the text area is empty
        if st.button('Ask a Question', disabled=(user_prompt == "")):
            # Display a progress bar
            with st.spinner('Processing...'):
                progress_bar = st.progress(0)

                # Simulate progress
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                    

                client = OpenAI(
                    # This is the default and can be omitted
                    api_key=os.environ.get("OPENAI_API_KEY"),
                )
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": f"Based on the following text: {file_content}, {user_prompt}"}]
                )
                summary = response.choices[0].message.content
                st.write(summary)

            # Remove the progress bar after processing
            progress_bar.empty()