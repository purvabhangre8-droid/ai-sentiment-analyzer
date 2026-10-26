import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
st.set_page_config(
page_title="AI Sentiment Analyzer",
page_icon="💬",
layout="centered"
)
st.title("💬 AI Sentiment Analyzer")
st.write(
"Enter a sentence, review, or comment below. "
"This NLP application will identify its sentiment."
)
@st.cache_resource
def load_analyzer():
return SentimentIntensityAnalyzer()
analyzer = load_analyzer()
text = st.text_area(
"Enter your text here:",
placeholder="Example: I absolutely love this product!",
height=150
)
if st.button("Analyze Sentiment", type="primary"):
if not text.strip():
st.warning("Please enter some text first.")
else:
scores = analyzer.polarity_scores(text)
compound = scores["compound"]
    if compound >= 0.05:
        sentiment = "Positive 😊"
        st.success(f"Sentiment: {sentiment}")
    elif compound <= -0.05:
        sentiment = "Negative 😞"
        st.error(f"Sentiment: {sentiment}")
    else:
        sentiment = "Neutral 😐"
        st.info(f"Sentiment: {sentiment}")

    st.metric("Sentiment Score", f"{compound:.3f}")

    st.subheader("Detailed NLP Scores")
    st.write(f"Positive: {scores['pos']:.3f}")
    st.write(f"Neutral: {scores['neu']:.3f}")
    st.write(f"Negative: {scores['neg']:.3f}")

    st.caption(
        "This educational application uses VADER sentiment analysis."
    )
st.divider()
st.caption("NLP College Assignment | AI Sentiment Analyzer")
