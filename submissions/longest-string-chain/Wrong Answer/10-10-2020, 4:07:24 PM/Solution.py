// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
#         """
#         method 1: DP + List : TLE
#         """
#         words = list(set(words))
#         def ispredecessor(word1, word2):
#             i, j, n1, n2, cnt = 0, 0, len(word1), len(word2), 0
#             while i < n1 and j < n2:
#                 if word1[i] != word2[j]:
#                     j += 1
#                     cnt += 1
#                     continue
#                 i += 1
#                 j += 1
#             if cnt == 0 and j == n2 - 1:
#                 cnt += 1
#                 j += 1
#             return False if cnt > 1 or i != n1 or j != n2 else True
        
#         words.sort(key=lambda x: len(x))
#         n = len(words)
#         dp = [1 for _ in range(n)]
        
#         for i in range(n):
#             for j in range(i):
#                 if ispredecessor(words[j], words[i]):
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
    
        """
        method 2: DP + dict
        """
        def longestStrChain(self, words):
            dp = {}
            for w in sorted(words, key=len):
                dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
            return max(dp.values())