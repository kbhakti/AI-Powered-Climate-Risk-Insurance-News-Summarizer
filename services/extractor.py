import re

def extract_insights(summary):
    if ((summary == "") or ("i can only assist with climate risk" in summary.lower())) :
        return {}
    
    # Lowercase copy for pattern matching
    text = summary.lower()

    # Predefined risk-related keywords (you can extend this list)
    risk_keywords = [
        "climate", "flood", "drought", "storm", "wildfire", "disaster", "cyclone",
        "emissions", "carbon", "greenhouse", "insurance", "reinsurance", "loss", "damage"
    ]

    # Extract risk factors (unique and matched in context)
    risk_factors = list(set([
        word for word in risk_keywords if word in text
    ]))

    # Define a basic list of stop words to exclude
    stop_words = {
        "The", "A", "An", "In", "On", "At", "It", "He", "She", "They", "We", "I",
        "And", "But", "Or", "Of", "To", "For", "By", "As", "From", "With", "Not"
    }

    # Extract capitalized word sequences (e.g., "New Delhi", "United Nations")
    raw_locations = re.findall(r"\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,})*", summary)

    # Filter out any matches that are stop words or contain stop words only
    locations = list(set([
        loc for loc in raw_locations if all(word not in stop_words for word in loc.split())
    ]))

    # Sentiment (basic rule-based detection — can be replaced with LLM-based)
    if any(w in text for w in ["catastrophic", "severe", "worst", "crisis", "alarming", "threat"]):
        sentiment = "Negative"
    elif any(w in text for w in ["progress", "resilient", "recovery", "adapt", "mitigate", "opportunity"]):
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    # Extract keywords that imply actions or responses
    actions = re.findall(r"\b(adopt|mitigate|prepare|respond|insure|warn|adapt|evacuate|declare)\b", text)

    return {
        "risk_factors": risk_factors,
        "locations": locations,
        "sentiment": sentiment,
        "actions": list(set(actions))  # de-duplicate
    }
