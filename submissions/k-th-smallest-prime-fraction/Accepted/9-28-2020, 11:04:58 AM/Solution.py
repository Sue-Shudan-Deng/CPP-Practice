// https://leetcode.com/problems/k-th-smallest-prime-fraction

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        def under(x):
            num, best = 0, (0, n - 1)
            i = -1
            for j in range(1, n):
                while x >= A[i+1] / A[j]:
                    i += 1
                num += i + 1
                if i >= 0 and A[i] / A[j] >= A[best[0]] / A[best[1]]:
                    best = (i, j)
            return num, best
        
        l, r = 0.0, 1.0
        best = (0, n - 1)
        while l < r - 1e-9:
            m = l + (r - l) / 2.0
            num, ans = under(m)
            if num >= K:
                best = ans
                print(num, best, l, r, m)
                print("""""""""""""""""")
                r = m
            else:
                l = m
        return [A[best[0]], A[best[1]]]
                