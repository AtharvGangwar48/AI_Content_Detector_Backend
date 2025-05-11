from data.common_phrases import common_phrases

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PhraseTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, phrase):
        node = self.root
        for word in phrase.split():
            node = node.children.setdefault(word, TrieNode())
        node.is_end = True

    def count_matches(self, tokens):
        count = 0
        n = len(tokens)
        for i in range(n):
            node = self.root
            j = i
            while j < n and tokens[j] in node.children:
                node = node.children[tokens[j]]
                if node.is_end:
                    count += 1
                j += 1
        return count

trie = PhraseTrie()
for phrase in common_phrases:
    trie.insert(phrase)