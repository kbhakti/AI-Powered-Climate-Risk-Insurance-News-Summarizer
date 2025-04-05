from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from config.settings import OPENAI_API_KEY

# Initialize LLM
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing. Please check your .env file.")
llm = OpenAI(temperature=0.3, api_key=OPENAI_API_KEY)

# Optional: prompt template
template = """
You are an expert in climate risk and insurance domain.

Determine whether the following topic is related to climate risk, climate change impacts, sustainability, or insurance:

"{text}"

If it is related, respond with "Yes".
If it is not related, respond with:
"I can only assist with climate risk and insurance-related information."
"""
prompt = PromptTemplate.from_template(template)

def check_input(text):
    #print(prompt.format(text=text))
    return llm.invoke(prompt.format(text=text))


