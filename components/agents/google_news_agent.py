import requests
from config.settings import NEWS_API_KEY

ENDPOINT = "https://newsapi.org/v2/everything"

async def fetch_google_news(topic):
    url = f"{ENDPOINT}?q={topic}&apiKey={NEWS_API_KEY}&language=en"
    response = requests.get(url)
    data = response.json()
    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item["title"],
            "content": item["content"] or item["description"]
        })
    return articles
