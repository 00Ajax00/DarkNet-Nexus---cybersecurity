# ml_models/sentiment_model.py
from textblob import TextBlob

class SentimentModel:
    @staticmethod
    def analyze(text):
        blob = TextBlob(text)
        return {
            "polarity": blob.sentiment.polarity,
            "subjectivity": blob.sentiment.subjectivity,
            "sentiment": "positive" if blob.sentiment.polarity > 0 else "negative"
        }

# Usage
# print(SentimentModel.analyze("This is an amazing product!"))
