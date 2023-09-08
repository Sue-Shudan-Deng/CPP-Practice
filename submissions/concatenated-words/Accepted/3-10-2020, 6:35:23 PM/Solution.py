// https://leetcode.com/problems/concatenated-words

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        mem = {}
        
        def dfs(word: str):
            """
            之前貌似有视频讲解用了同样的思路
            """
            if word in mem:
                return True
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and (suffix in words or dfs(suffix)):
                    mem[word] = True
                    return True
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res