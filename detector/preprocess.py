import re
import nltk
nltk.data.path.append("./nltk_data")
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return [word for word in tokens if word not in STOPWORDS]
