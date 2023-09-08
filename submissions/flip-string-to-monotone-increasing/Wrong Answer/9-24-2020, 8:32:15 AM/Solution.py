// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n, ans = len(S), float("inf")
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        
        for i in range(1, n):
            l[i] = l[i-1] + (S[i] == "1")
            
        for j in range(0, n-1):
            r[j] = r[j+1] + (S[j] == "0")
            
        for i in range(n):
            ans = min(ans, l[i] + r[i])
        
        return ans