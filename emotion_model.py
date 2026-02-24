import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def detect_emotion(text):
    sentiment_score = sia.polarity_scores(text)["compound"]

    if sentiment_score >= 0.5:
        emotion = "Positive"
    elif sentiment_score >= 0.1:
        emotion = "Mildly Positive"
    elif sentiment_score <= -0.5:
        emotion = "Negative"
    elif sentiment_score <= -0.1:
        emotion = "Mildly Negative"
    else:
        emotion = "Neutral"

    return emotion, sentiment_score