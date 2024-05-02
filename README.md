# Fake-News-Detection-Streamlit-Web-App
This web application is designed to predict whether a given news article is fake or real. It utilizes machine learning techniques, specifically logistic regression, trained on a dataset of news articles labeled as fake or real.

# How It Works
- Input: Users can input a news article text into the provided text area.
- Prediction: The app preprocesses the input text by removing stopwords, stemming, and vectorizing it using TF-IDF. Then, it predicts whether the article is fake or real using a logistic regression model.
- Output: The app displays the prediction result - either "Fake News" or "Real News" - based on the model's classification.

# Dataset
The model is trained on a dataset sourced from [kaggle](https://www.kaggle.com/c/fake-news/data). The dataset contains labeled news articles, where each article is classified as either fake or real.

# Dependencies
- Python 3.x
- Streamlit
- NLTK
- Scikit-learn
- Pandas
- NumPy

# Usage
To use the app:

1. Clone the repository to your local machine.
2. Install the required dependencies by running pip install -r requirements.txt.
3. Run the app using Streamlit by executing streamlit run app.py in your terminal.
4. Enter the news article text into the text area and click on "Predict".
5. View the prediction result displayed on the app.

# Sample Predictions

## Real News Prediction
### This screenshot shows an example of the app predicting a news article as "Real News".
![fake news real news](https://github.com/EktaTripathi/Fake-News-Detection-Streamlit-Web-App/assets/94041887/33ad1fd7-b202-425a-850e-ecc2646361b4)

## Fake News Prediction
### This screenshot demonstrates an example of the app predicting a news article as "Fake News".
![fake news fake news](https://github.com/EktaTripathi/Fake-News-Detection-Streamlit-Web-App/assets/94041887/cf0ad7ad-6fbf-46c3-ad8e-a3217a09a934)
