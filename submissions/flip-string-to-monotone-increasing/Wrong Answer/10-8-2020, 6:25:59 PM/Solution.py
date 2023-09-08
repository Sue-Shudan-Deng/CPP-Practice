// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        l = [0 for _ in range(n + 1)]
        r = [0 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            l[i] = l[i-1] + (S[i-1] == "1")
            
        for j in range(n, 1, -1):
            r[j-1] = r[j] + (S[j-1] == "0")
        
        ans = n
        for i in range(1, n + 1):
            ans = min(ans, l[i] + r[i])
        
        return ans