// https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # build trie
        trie = {}
        for w in dictionary:
            node = trie
            for c in w:
                if not c in node:
                    node[c] = {}
                node = node[c]
            node['#'] = w
            
        def search(word):
            node = trie
            for c in word:
                if '#' in node:
                    return node['#']
                if not c in node:
                    return word
                node = node[c]
            return word                  
        
        ans = []
        for word in sentence.split():
            ans.append(search(word))
        return " ".join(ans)