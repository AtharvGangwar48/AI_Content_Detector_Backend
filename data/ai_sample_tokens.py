import pandas as pd
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# Read CSV file
df = pd.read_csv('data/Training_Essay_Data.csv')

ai_sample_tokens = []

# Assuming the text is in a column named 'text'. Change as needed.
for text in df.iloc[:, 0]:  # Or df['column_name'] if you know it
    ai_sample_tokens.extend(preprocess(str(text)))
