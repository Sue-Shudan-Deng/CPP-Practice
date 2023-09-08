// https://leetcode.com/problems/minimum-cost-to-connect-sticks

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sticks.sort(key = lambda s: -s)
        res = 0
        for i, s in enumerate(sticks):
            res += s * (i + 1)
        return res - s