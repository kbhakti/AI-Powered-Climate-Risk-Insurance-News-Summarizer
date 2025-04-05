from langchain_openai import OpenAI
from config.settings import OPENAI_API_KEY

llm = OpenAI(temperature=0.3, api_key=OPENAI_API_KEY)

def evaluate_summary(summary):
    if ((summary == "") or ("i can only assist with climate risk" in summary.lower())) :
        return {}
    # 1. Length scoring (ideal: 100–150 words)
    word_count = len(summary.split())
    if word_count < 80:
        length_score = 2
    elif 80 <= word_count <= 160:
        length_score = 5
    elif 160 < word_count <= 250:
        length_score = 4
    else:
        length_score = 3

    # 2. Use LLM to evaluate clarity and accuracy
    eval_prompt = f"""
    You are evaluating the following summary for clarity and factual accuracy.

    Summary:
    {summary}

    Rate each category from 1 (poor) to 5 (excellent) and explain why:

    - Clarity Score:
    - Accuracy Score:
    - Justification (1 line per score):
    """
    llm_response = llm.invoke(eval_prompt)

    # Extract scores using basic regex (can be enhanced)
    import re
    clarity_match = re.search(r"Clarity Score:\s*(\d)", llm_response)
    accuracy_match = re.search(r"Accuracy Score:\s*(\d)", llm_response)

    clarity_score = int(clarity_match.group(1)) if clarity_match else 3
    accuracy_score = int(accuracy_match.group(1)) if accuracy_match else 3

    # Optional: extract justifications
    justifications = re.findall(r"Justification.*?:\s*(.*)", llm_response, re.I)

    # Calculate total score (out of 15)
    total = clarity_score + accuracy_score + length_score
    grade = "Excellent" if total >= 13 else "Good" if total >= 10 else "Needs Improvement"

    return {
        "length_score": length_score,
        "clarity_score": clarity_score,
        "accuracy_score": accuracy_score,
        "total_score": total,
        "grade": grade,
        "justification": justifications[0] if justifications else "N/A"
    }
