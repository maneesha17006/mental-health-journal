import pandas as pd
import numpy as np
import plotly.express as px

def rolling_average(df):
    df["rolling_sentiment"] = df["sentiment"].rolling(window=7).mean()
    return df

def emotional_volatility(df):
    return round(df["sentiment"].std(), 3)

def stability_score(df):
    volatility = df["sentiment"].std()
    return round(max(0, 100 - (volatility * 100)), 1)

def negative_streak(df):
    streak = 0
    max_streak = 0

    for val in df["sentiment"]:
        if val < 0:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    return max_streak

def burnout_risk(df):
    recent = df.tail(7)
    ratio = (recent["sentiment"] < 0).mean()

    if ratio > 0.6:
        return "High"
    elif ratio > 0.4:
        return "Moderate"
    else:
        return "Low"

def summary_report(df):
    stability = stability_score(df)
    volatility = emotional_volatility(df)
    streak = negative_streak(df)
    risk = burnout_risk(df)

    return f"""
Emotional Stability Score: {stability}/100
Volatility Index: {volatility}
Longest Negative Streak: {streak} entries
Burnout Risk Level: {risk}

If negative streaks persist or risk remains high,
professional mental health support should be considered.
"""

def sentiment_line_chart(df):
    fig = px.line(
        df,
        x="date",
        y="sentiment",
        height=350
    )
    return fig