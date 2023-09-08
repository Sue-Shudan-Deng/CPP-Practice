// https://leetcode.com/problems/word-squares

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n, res = len(words[0]), []
        def getWordWithPrefix(prefix):
            for w in words:
                if w.startswith(prefix):
                    yield w
        
        def dfs(w, cur, res):
            if len(cur) == n:
                res.append(copy.deepcopy(cur))
                return
            prefix = "".join([i[len(cur)] for i in cur])
            for next_w in getWordWithPrefix(prefix):
                cur.append(next_w)
                dfs(next_w, cur, res)
                cur.pop()
        
        for w in words:
            dfs(w, [w], res)
        return res