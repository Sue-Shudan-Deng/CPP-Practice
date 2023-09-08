// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # step 1: check if letters or counts match
        if len(s1) + len(s2) != len(s3):
            return False
        s1_counter = collections.Counter(s1)
        s2_counter = collections.Counter(s2)
        s3_counter = collections.Counter(s3)
        for k, v in s3_counter.items():
            if s1_counter.get(k, 0) + s2_counter.get(k, 0) != v:
                return False
        
        # step 2: dp
        # dp[i][j], whether s3[:i+j] is the interleaving of s1[:i] and s2[:j]
        n1, n2 = len(s1), len(s2)
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True
        
        for i in range(1, n1 + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n2 + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
                
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s3[i+j-1] == s1[i-1]:
                    dp[i][j] = dp[i-1][j]
                if s3[i+j-1] == s2[j-1]:
                    dp[i][j] |= dp[i][j-1]
        return dp[-1][-1]