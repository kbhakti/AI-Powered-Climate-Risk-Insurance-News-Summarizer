from langchain_community.tools.tavily_search import TavilySearchResults

async def fetch_tavily_news(topic):
    try:
        tool = TavilySearchResults(
        tavily_api_key="BV0rt",
        max_results=100,
        search_depth='advanced',
        include_answer=True,
        include_raw_content=True,
        include_images=True,
        )
        response = tool.invoke({'query': topic})
        return response
    except Exception as e:
        print(f"Error in fetch_tavily_news: {e}")
        return []  # Return empty list instead of None
