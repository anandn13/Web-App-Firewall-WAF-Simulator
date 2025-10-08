import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

MODEL_FILE = "ml_model.pkl"

def train_model():
    # Sample dataset
    data = [
        ("SELECT * FROM users WHERE id = 1", "SQLi"),
        ("<script>alert('XSS')</script>", "XSS"),
        ("Robert'); DROP TABLE Students;--", "SQLi"),
        ("Hello, world!", "Normal"),
        ("<img src=x onerror=alert('XSS')>", "XSS"),
        ("admin' --", "SQLi"),
        ("Welcome to the homepage.", "Normal"),
        ("javascript:alert('XSS')", "XSS"),
        ("DROP DATABASE test;", "SQLi"),
        ("Normal user message", "Normal"),
    ]
    df = pd.DataFrame(data, columns=["payload", "label"])
    X = df["payload"]
    y = df["label"]
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)
    clf = MultinomialNB()
    clf.fit(X_vec, y)
    # Save model
    with open(MODEL_FILE, "wb") as f:
        pickle.dump((vectorizer, clf), f)

def predict_attack(payload: str):
    if not os.path.exists(MODEL_FILE):
        train_model()
    with open(MODEL_FILE, "rb") as f:
        vectorizer, clf = pickle.load(f)
    X_vec = vectorizer.transform([payload])
    pred = clf.predict(X_vec)[0]
    return pred