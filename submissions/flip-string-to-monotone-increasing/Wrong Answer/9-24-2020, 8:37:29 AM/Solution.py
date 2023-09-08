// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n, ans = len(S), float("inf")
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        
        l[0] = (S[0] == "1")
        for i in range(1, n):
            l[i] = l[i-1] + (S[i] == "1")
            
        r[-1] = (S[-1] == "0")
        for j in range(n-2, -1, -1):
            r[j] = r[j+1] + (S[j] == "0")
            
        for i in range(n):
            ans = min(ans, l[i-1] + r[i])
        
        return ans