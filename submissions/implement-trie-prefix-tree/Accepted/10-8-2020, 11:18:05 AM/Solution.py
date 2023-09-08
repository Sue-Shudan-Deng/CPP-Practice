// https://leetcode.com/problems/implement-trie-prefix-tree

"""
Python的实现用hashmap, C++的实现用array + unique_ptr
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            if not c in p:
                p[c] = {}
            p = p[c]
        p['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.find(word)
        return p and '#' in p

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix)
        
    def find(self, prefix):
        p = self.root
        for c in prefix:
            if not c in p:
                return None
            p = p[c]
        # 貌似这里的p不是None而是至少有一个p['#'] = True
        return p

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)