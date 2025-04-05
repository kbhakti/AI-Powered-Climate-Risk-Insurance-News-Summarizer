from services.summarizer import summarize_text
from services.extractor import extract_insights
from services.evaluator import evaluate_summary
from utils.parser import parse_uploaded_file
from utils.chunker import split_text

def process_input(input_type, input_data):
    if input_type == "upload":
        combined_text = parse_uploaded_file(input_data)
    else:
        combined_text = input_data

    chunks = split_text(combined_text)
    intermediate_summaries = [summarize_text(chunk, "intermediate") for chunk in chunks]
    full_summary = summarize_text(" ".join(intermediate_summaries), "full")

    #print("full_summary", full_summary)
    insights = extract_insights(full_summary)
    evaluation = evaluate_summary(full_summary)

    return {
        "summary": full_summary,
        "insights": insights,
        "evaluation": evaluation
    }


