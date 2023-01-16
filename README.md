# Sentiment Analysis Model

This project is a sentiment analysis model that can classify text as positive or negative. The model is trained on a dataset of movie reviews and can be used to classify the sentiment of any text.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- scikit-learn
- pandas
- numpy
- pickle

### Installing

Clone the repository and install the dependencies using pip:

```bash
git clone https://github.com/Sultan-aj/Sentiment-Analysis.git
pip install -r requirements.txt
```

### Running the model

To use the model, you can use the provided `predict.py` script to classify the sentiment of a single text.

1. Open the `predict.py` script in your text editor.
2. Locate the following line:
```bash
with open("insert_your_file_path_here", "r") as f:
```
3. Replace `'insert_your_file_path_here'` with the path to your text file.
```bash
with open("path/to/text_file.txt", "r") as f:
```
4. Save the changes to the `predict.py` script.
5. Run the script by typing the following command in your terminal:
```bash
python predict.py
```


## Built With

* [Scikit-learn](https://scikit-learn.org/) - The machine learning library used
* [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
* [Numpy](https://numpy.org/) - Scientific computing with Python
* [Pickle](https://docs.python.org/3/library/pickle.html) - Serialization of the trained model

## Author

* **Sultan.aj** - [https://github.com/Sultan-aj](https://github.com/Sultan-aj)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
