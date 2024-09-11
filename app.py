import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained model, vectorizer, and label encoder
@st.cache_resource
def load_model():
    model = pickle.load(open('sentiment_analysis_model.h5', 'rb'))
    vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
    label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))
    return model, vectorizer, label_encoder

# Define Streamlit app
def main():
    # App title
    st.title("News Sentiment Analysis")
    
    # Instructions
    st.write("Enter news text below to predict its sentiment:")
    
    # Text input
    text_input = st.text_area("News Text", height=150)
    
    # Load the model, vectorizer, and label encoder
    model, vectorizer, label_encoder = load_model()

    # When the user submits text
    if st.button("Predict Sentiment"):
        if text_input:
            # Transform the input text
            text_input_tfidf = vectorizer.transform([text_input])
            
            # Predict sentiment
            prediction = model.predict(text_input_tfidf)
            predicted_sentiment = label_encoder.inverse_transform(prediction)[0]
            
            # Display result
            st.success(f"Predicted sentiment: {predicted_sentiment}")
        else:
            st.warning("Please enter some news text to analyze.")

# Run the app
if __name__ == "__main__":
    main()