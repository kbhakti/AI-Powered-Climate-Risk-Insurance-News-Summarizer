from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from config.settings import OPENAI_API_KEY

# Initialize LLM
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing. Please check your .env file.")
llm = OpenAI(temperature=0.3, api_key=OPENAI_API_KEY)

# Optional: prompt template
template = """
You are an expert in climate risk and insurance news analysis. Your job is to:
- Analyze a given article
- Generate a structured summary focused on climate risk or insurance
- Evaluate the summary based on specific criteria

Instructions:
- Do not add any facts that are not found in the original article.
- Only include insights related to climate risk, sustainability, or insurance.
- Keep the summary objective, relevant, and concise.

Step 1: Determine whether the article below is related to climate risk, climate change, sustainability, or insurance.

If it is **NOT** related, respond with:
"⚠️ I can only assist with climate risk and insurance-related information."

If it **IS** related, proceed to Step 2.

Step 2: Summarize the article in **{no_of_sentences} sentences**.

Article:
{text}
"""

prompt = PromptTemplate.from_template(template)

def summarize_text(text,type="intermediate"):
    if not text.strip():
        return "⚠️ No content to summarize."
    if len(text.split()) < 20:
        return f"⚠️ Text too short to summarize: {text}"
    
    if(type == "intermediate"):
        no_of_sentences = "2"
    else :
        no_of_sentences = "10"

    #print(prompt.format(text=text,no_of_sentences=no_of_sentences))
    return llm.invoke(prompt.format(text=text,no_of_sentences=no_of_sentences))


