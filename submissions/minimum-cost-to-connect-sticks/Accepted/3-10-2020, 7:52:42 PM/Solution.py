// https://leetcode.com/problems/minimum-cost-to-connect-sticks

from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        就是Huffman编码
        """
        heapify(sticks)
        res = 0
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            res += (x + y)
            heappush(sticks, x + y)
        return res