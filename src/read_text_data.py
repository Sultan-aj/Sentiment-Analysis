import pandas as pd
import os


def read_text_data(data_dir):

    if os.path.exists(data_dir):
        print('The path exists')
    else:
        print('The path does not exist')
        return
        

    # Create an empty list to store the text data
    text_data = []

    # Iterate over the text files in the dataset directory
    for file in os.listdir(data_dir):
        # Read the text from the file
        with open(os.path.join(data_dir, file), 'r', encoding='utf-8') as f:
            text = f.read()
        # Add the text to the list
        text_data.append(text)

    # Convert the list to a Pandas dataframe
    df = pd.DataFrame(text_data, columns=['text'])
    
    return df

# df = read_text_data("C:\\Users\\sulta\\OneDrive\\Desktop\\Python\\SentimentAnalysis\\data\\aclImdb\\train\\pos")
# print(df)