import streamlit as st

def select_input_mode():
    mode = st.radio("Choose input type", ["Scraped News", "Upload Report"])
    if mode == "Scraped News":
        topic = st.text_input("Enter a topic to search for:")
        return "scraped", topic
    else:
        uploaded_file = st.file_uploader("Upload a report (PDF or TXT)", type=["pdf", "txt"])
        return "upload", uploaded_file
