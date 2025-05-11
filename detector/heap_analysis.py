from collections import Counter
import heapq

def top_k_frequent(tokens, k=5):
    freq = Counter(tokens)
    return heapq.nlargest(k, freq.items(), key=lambda x: x[1])