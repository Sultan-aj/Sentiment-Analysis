import numpy as np
import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from merge_df import merge_df

# Load the dataset
if os.path.exists('../sentiment_data.csv'):
    print("sentiment_data.csv exists")
    data = pd.read_csv("../sentiment_data.csv")
else:
    print("sentiment_data does not exists")
    data = merge_df()

data = data.dropna()

# Split the dataset into features (X) and labels (y)
X = data['text']
y = data['sentiment']


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the model to a file
with open("../models/sentiment_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

# Make predictions on the test set
y_pred = model.predict(X_test)


# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))