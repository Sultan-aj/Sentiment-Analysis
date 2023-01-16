import nltk
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
from read_text_data import read_text_data
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')
# def preprocess(data):
#     text_data = []
#     my_list = []
#     my_list.append(data)
#     index = len(my_list)
#     i = 0
#     while i < index:
#         text = my_list[i]
#         # Tokenize the text
#         tokens = nltk.word_tokenize(text)

#         # Remove punctuation and convert to lowercase
#         tokens = [token.lower() for token in tokens if token.isalpha()]

#         # Remove stop words
#         stop_words = nltk.corpus.stopwords.words('english')
#         tokens = [token for token in tokens if token not in stop_words]

#         # Stem the tokens
#         stemmer = nltk.stem.PorterStemmer()
#         tokens = [stemmer.stem(token) for token in tokens]
#         for word in tokens:
#             text_data.append(word)
#         i = i+1
    # # new_df = pd.DataFrame(text_data, columns=['text'], index=None)
    # new_df = pd.DataFrame({'text': text_data, 'sentiment': 'positive'}, index=None)

    # return new_df

    # Define a function to preprocess the text
def preprocess_text(text):
    # Remove special characters and HTML tags
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Lowercase the text
    text = text.lower()
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if w not in stop_words]
    # Stem the words
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(w) for w in words]
    # Join the stemmed words
    preprocessed_text = " ".join(stemmed_words)
    return preprocessed_text


    

# # Example usage
# df = read_text_data("C:\\Users\\sulta\\OneDrive\\Desktop\\Python\\SentimentAnalysis\\data\\aclImdb\\train\\pos")
# # print(df['text'].to_string(index=False))
# df = df['text'].to_string(index=False)
# tokens = pd.DataFrame(preprocess(df))
# tokens.to_csv('test.csv')

