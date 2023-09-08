// https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones: 
            heapq.heappush(maxheap, -stone)
        while len(maxheap) > 1:
            x1 = heapq.heappop(maxheap)
            x2 = heapq.heappop(maxheap)
            heapq.heappush(maxheap, - abs(x1-x2))
        return -maxheap[0]