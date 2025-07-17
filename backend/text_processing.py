import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess_text(text):
    words = word_tokenize(text.lower())  # Convert to lowercase & tokenize
    print(f"Processed Words: {words}")  # Debugging log
    return words

if __name__ == "__main__":
    print(preprocess_text("Hello, how are you?"))
