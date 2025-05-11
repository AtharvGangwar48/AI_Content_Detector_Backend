import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# Add more examples to improve robustness
ai_samples = [
    "in conclusion it is important to note that artificial intelligence is revolutionizing the world",
    "furthermore this technology enables greater automation and efficiency across industries",
    "therefore we can expect continued innovation in machine learning and data analysis",
    "moreover the impact of ai on society is growing rapidly with significant implications",
    "as a result businesses are increasingly integrating ai tools into their workflows"
]

# Tokenize all phrases and flatten into a single list of tokens
ai_sample_tokens = []
for sentence in ai_samples:
    ai_sample_tokens.extend(preprocess(sentence))
