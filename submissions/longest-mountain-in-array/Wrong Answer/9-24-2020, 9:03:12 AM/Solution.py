// https://leetcode.com/problems/longest-mountain-in-array

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        
        l[0] = 1
        for i in range(1, n):
            l[i] = l[i-1] + 1 if A[i] > A[i-1] else 1
        
        r[-1] = 1
        for i in range(n-2, -1, -1):
            r[i] = r[i+1] + 1 if A[i] > A[i+1] else 1
            
        ans = 0
        for i in range(n):
            ans = max(ans, l[i] + r[i] - 1)
        return ans