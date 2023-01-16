import pickle
from sklearn.feature_extraction.text import CountVectorizer


def predict_sentiment(text):
    # Load the pre-trained model from a file
    with open("../models/sentiment_model.pkl", "rb") as f:
        model,vectorizer  = pickle.load(f)

    # Vectorize the input text
    # vectorizer = CountVectorizer()
    x = vectorizer.transform([text])

    # Make a prediction
    y_pred = model.predict(x)[0]

    return y_pred

# Test the function
text = "This is a great movie!"
try:
    with open("../data/aclImdb/test/pos/19_10.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied.")

print(text)
print("Sentiment:", predict_sentiment(text))
