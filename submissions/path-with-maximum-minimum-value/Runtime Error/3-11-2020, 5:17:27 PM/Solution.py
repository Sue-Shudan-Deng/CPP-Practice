// https://leetcode.com/problems/path-with-maximum-minimum-value

from heapq import *
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if 0 <= nr < row and 0 <= nc < col:
                    yield nr, nc
                    
        maxHeap = [(-A[0][0], 0, 0)]
        seen = set()
        while maxHeap:
            val, r, c = heappop(maxHeap)
            if r == row - 1 and c == col - 1:
                return -val
            for nr, nc in neighbors(r, c):
                if not (nr, nc) in seen:
                    seen.add((nr, nc))
                    heappush(maxHeap, (max(val, A[nr, nc]), nr, nc))
        return -1