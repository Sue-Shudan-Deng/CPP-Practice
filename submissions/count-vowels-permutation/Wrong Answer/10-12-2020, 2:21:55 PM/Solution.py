// https://leetcode.com/problems/count-vowels-permutation

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        没看出和knight dialer 935有啥区别
        """
        mapping = {"a": ["e"], "e": ["a", "i"], "i": ["a", "e", "o", "u"], 
                  "o": ["i", "u"], "u": ["a"]}
        vowels = {"a":0, "e":1, "i":2, "o":3, "u":4}
        dp = [[0 for _ in range(5)] for _ in range(n + 1)]
        # dp[i][j]: 长度为i以vowels[j]结尾的有多少个
        for i in range(1, n + 1):
            for k, v in mapping.items():
                if i == 1:
                    dp[1][vowels[k]] += 1
                else:
                    for nei in v:
                        dp[i][vowels[nei]] += dp[i-1][vowels[k]]
        return sum(dp[n])