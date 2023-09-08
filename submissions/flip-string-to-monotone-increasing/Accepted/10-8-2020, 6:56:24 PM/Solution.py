// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
#     def minFlipsMonoIncr(self, S: str) -> int:
#         """
#         method 1: 1d DP
#         """
#         n = len(S)
#         l = [0 for _ in range(n + 1)]
#         r = [0 for _ in range(n + 1)]
        
#         for i in range(1, n + 1):
#             l[i] = l[i-1] + (S[i-1] == "1")
            
#         for j in range(n-1, 0, -1):
#             r[j] = r[j+1] + (S[j] == "0")
        
#         """
#         l和r都是考虑了包含index自身
#         """
        
#         ans = n
#         for i in range(1, n + 1):
#             ans = min(ans, l[i-1] + r[i])
        
#         return ans
    
    def minFlipsMonoIncr(self, S: str) -> int:
        """
        method 2: 2d DP
        """
        n = len(S)
        dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        
        # dp[0][*]: To make this char 0
        # dp[1][*]: To make this char 1
        
        for i in range(1, n + 1):
            if S[i-1] == '0':
                dp[0][i] = dp[0][i-1]
                dp[1][i] = min(dp[0][i-1], dp[1][i-1]) + 1
            else:
                dp[0][i] = dp[0][i-1] + 1
                dp[1][i] = min(dp[0][i-1], dp[1][i-1])
        
        return min(dp[0][-1], dp[1][-1])
    
        