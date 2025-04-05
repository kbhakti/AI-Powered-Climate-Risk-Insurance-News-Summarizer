# 🌍 AI-Powered Climate Risk & Insurance News Summarizer

This project is a Streamlit-based GenAI application that:
- Scrapes climate risk and insurance-related news
- Summarizes documents using LLMs
- Extracts key insights
- Evaluates the extracted summary

## 🚀 Features

- 🔎 Async scraping from Google News/Tavily Search
- 🧠 Summarization using openAI model
- 📊 Evaluation metrics for generated summaries
- 📄 PDF and text file upload support

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <this_repo_url>
   cd ai_news_summarizer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up `.env` in `config/` Folder**
   Create a file `config/.env` and add:
   ```
   OPENAI_API_KEY=your_openai_key
   NEWS_API_KEY=your_newsapi_key
   TAVILY_API_KEY=your_tavily_key
   ```

4. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

A browser tab will open with the app running at:

```
http://localhost:8501
```

### ❗ If You See Warnings or Errors

- Make sure Python is added to your `PATH` environment variable
- If the virtual environment(Ex:venv) doesn’t activate, try manually:
```bash
venv\Scripts\activate
```
## 🤖 Technologies Used

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT Models](https://platform.openai.com/)
- [Hugging Face Transformers](https://huggingface.co/)
- [Tavily](https://app.tavily.com)
- [GoogleNewsAPI](https://newsapi.org/s/google-news-api)

## 💬 Future Enhancements

- Semantic filters (e.g., location, date range)
- User-authenticated dashboards
- Human-in-the-loop feedback scoring
- Fine-tuning summarization with domain datasets

---

Made By Bhakti Kanungo
