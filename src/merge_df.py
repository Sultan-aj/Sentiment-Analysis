import pandas as pd
from read_text_data import read_text_data
from preprocess import preprocess_text
import os 

def merge_df():

    # Create a dataframe for positive text samples
    pos_texts = [ ... ]  # list of positive text samples
    pos_df = read_text_data("C:\\Users\\sulta\\OneDrive\\Desktop\\Python\\SentimentAnalysis\\data\\aclImdb\\train\\pos")
    #pos_processed = pd.DataFrame(preprocess(pos_df['text'].to_string(index=False)))
    pos_df['text'] = pos_df['text'].apply(preprocess_text)
    for text in pos_df["text"]:
        pos_texts.append(text)
    pos_df = pd.DataFrame({'text': pos_texts, 'sentiment': 'positive'})

    # Create a dataframe for negative text samples
    neg_texts = [ ... ]  # list of negative text samples
    neg_df = read_text_data("C:\\Users\\sulta\\OneDrive\\Desktop\\Python\\SentimentAnalysis\\data\\aclImdb\\train\\neg")
    neg_df['text'] = neg_df['text'].apply(preprocess_text)
    for text in neg_df["text"]:
        neg_texts.append(text)

    neg_df = pd.DataFrame({'text': neg_texts, 'sentiment': 'negative'})

    # Concatenate the two dataframes
    df = pd.concat([pos_df, neg_df], ignore_index=True)
    df.to_csv('sentiment_data.csv')
    print("file saved")

    return df

