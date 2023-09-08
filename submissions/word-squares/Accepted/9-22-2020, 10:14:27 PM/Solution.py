// https://leetcode.com/problems/word-squares

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n, res = len(words[0]), []
        prefixHashTable = defaultdict(set)
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                prefixHashTable[prefix].add(word)
        
        def getWordWithPrefix(prefix):
            """
            O(n), will TLE, optimized with hashtable 
            """
            # for w in words:
            #     if w.startswith(prefix):
            #         yield w
            if prefix in prefixHashTable:
                return prefixHashTable[prefix]
            else:
                return set([])
        
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