from transformers import pipeline

# Load a sentiment-analysis model
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english") # type: ignore

def analyze_sentiment(text):
    sentiment = model(text)
    result = sentiment[0]["label"].lower()
    return result