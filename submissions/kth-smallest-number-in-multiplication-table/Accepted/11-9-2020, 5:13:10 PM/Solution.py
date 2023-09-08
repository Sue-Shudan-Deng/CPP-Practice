// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table

class Solution:
    def findKthNumber(self, M, N, K):
        def enough(x):
            count = 0
            for i in range(1, M + 1):
                count += min(x // i, N)
            return count >= K

        l, r = 1, M * N
        while l < r:
            m = l + (r - l) // 2
            if enough(m):
                r = m
            else:
                l = m + 1
        return l