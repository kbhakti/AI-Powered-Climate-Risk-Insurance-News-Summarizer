import streamlit as st
from components.ui.loader import select_input_mode
from pipelines.processing_pipeline import process_input
from components.agents.agent_registry import get_all_articles_async
import asyncio
from services.check_input import check_input


st.set_page_config(page_title="AI Climate Risk Summarizer", layout="wide")
st.title("🌍 AI-Powered Climate Risk & Insurance News Summarizer")

input_type, input_data = select_input_mode()

if input_type == "scraped" and input_data:
    if st.button("🔎 Fetch Articles"):
        # 🧠 LLM-based validation inside the button logic
        validation_result = check_input(input_data)
        #print("validation_result:", validation_result)

        if "i can only assist with climate risk" in validation_result.lower():
            st.warning("⚠️ This topic is not related to climate risk or insurance. Please enter a relevant topic.")
            st.stop()
        with st.spinner("Scraping news..."):
            articles = asyncio.run(get_all_articles_async(input_data))
            text_data = "\n".join([a['content'] for a in articles])

            results = process_input("text", text_data)
            st.success("Done!")
            st.subheader("🧠 Summary")
            st.write(results['summary'])
            st.subheader("🔍 Key Insights")
            st.json(results['insights'])
            st.subheader("📊 Evaluation")
            st.write(results['evaluation'])


elif input_type == "upload" and input_data:
    with st.spinner("Processing document..."):
        results = process_input("upload", input_data)
        st.success("Done!")
        st.subheader("🧠 Summary")
        st.write(results['summary'])
        st.subheader("🔍 Key Insights")
        st.json(results['insights'])
        st.subheader("📊 Evaluation")
        st.write(results['evaluation'])