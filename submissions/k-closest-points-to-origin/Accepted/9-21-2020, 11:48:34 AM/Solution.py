// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # """
        # method 1: sort
        # """
        # return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]
        
        """
        method 2: minheap
        """
        
        def distance(x):
            return x[0] ** 2 + x[1] ** 2
        
        heap, n, ans = [], len(points), []
        for p in points:
            heapq.heappush(heap, (distance(p), p))
        for i in range(n-1, n-K-1, -1):
            ans.append(heapq.heappop(heap)[-1])
        return ans