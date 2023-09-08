// https://leetcode.com/problems/concatenated-words

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        def dfs(word: str):
            """
            之前貌似有视频讲解用了同样的思路
            """
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and (suffix in words or dfs(suffix)):
                    return True
            return False
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res