import asyncio
#  from components.agents.google_news_agent import fetch_google_news
from components.agents.tavily_agent import fetch_tavily_news

async def get_all_articles_async(topic):
    
    results = await asyncio.gather(
        #fetch_google_news(topic),
        fetch_tavily_news(topic)
    )

    # Filter out None values
    results = [r for r in results if r is not None]
    
    return [item for sublist in results for item in sublist]
