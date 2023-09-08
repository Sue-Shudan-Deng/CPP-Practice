// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def ispredecessor(word1, word2):
            i, j, n1, n2, cnt = 0, 0, len(word1), len(word2), 0
            while i < n1 and j < n2:
                if word1[i] != word2[j]:
                    j += 1
                    cnt += 1
                    continue
                i += 1
                j += 1
            return False if cnt > 1 or i != n1 or j != n2 else True
        
        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if ispredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)