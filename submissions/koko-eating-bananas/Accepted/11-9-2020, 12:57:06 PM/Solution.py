// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r, n = 1, max(piles), len(piles)
        while l < r:
            m = l + (r - l) // 2
            h = 0
            for i in range(n):
                h += (piles[i] + m - 1) // m
            if h <= H:
                r = m
            else:
                l = m + 1
        return l