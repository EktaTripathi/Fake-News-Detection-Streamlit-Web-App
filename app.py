import streamlit as st
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

# Load the model and vectorizer from disk

def load_model_and_vectorizer():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('Vector.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Define the stemming and preprocessing
def stemming(content):
    ps = PorterStemmer()
    stemmed_content = re.sub('[^a-zA-Z]', " ", content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [ps.stem(word) for word in stemmed_content if not word in set(stopwords.words('english'))]
    stemmed_content = " ".join(stemmed_content)
    return stemmed_content

# Title and description
st.title('Fake News Detection App')
st.write('This app predicts whether a news article is fake or real.')

# User input for prediction
user_input = st.text_area("Enter the news article text:", "",height=200)
if st.button('Predict'):
    if user_input:
        # Preprocess and predict
        processed_input = stemming(user_input)
        input_vector = vectorizer.transform([processed_input])
        prediction = model.predict(input_vector)
        if prediction[0] == 1:
            st.write("Prediction: Fake News")
        else:
            st.write("Prediction: Real News")
