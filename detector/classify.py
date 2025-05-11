from .preprocess import preprocess_text
from .hashing import word_frequency
from .trie_detector import trie, common_phrases
from .edit_distance import levenshtein_distance, ai_sample_tokens
from .heap_analysis import top_k_frequent
from data.ai_like_words import ai_like_words

def classify_text(text):
    tokens = preprocess_text(text)
    top_words = [w for w, _ in top_k_frequent(tokens)]

    # Feature 1: Hashing
    freq = word_frequency(tokens)

    # Feature 2: Trie Match
    phrase_matches = trie.count_matches(tokens)

    # Feature 3: Edit Distance
    distance = levenshtein_distance(tokens, ai_sample_tokens)
    similarity = 1 - (distance / max(len(tokens), len(ai_sample_tokens)))

    # Feature 4: Heap
    common_count = sum(1 for w in top_words if w in ai_like_words)

    # Final Scoring
    score = (
        0.3 * min(phrase_matches / 3, 1) +
        0.4 * similarity +
        0.3 * min(common_count / 3, 1)
    )

    label = "AI-Generated" if score > 0.6 else "Human-Written"
    return {
        "label": label,
        "confidence": round(score * 100, 2)
    }