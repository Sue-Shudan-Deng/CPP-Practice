// https://leetcode.com/problems/minimum-cost-to-hire-k-workers

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        """
        maxheap + greedy, 参考lee215的算法
        """
        n = len(quality)
        comb = [(float(wage[i]) / quality[i], quality[i]) for i in range(n)]
        comb.sort(key = lambda x: x[0])
        maxheap, qsum, res = [], 0, float("inf")
        
        for cur_ratio, q in comb:
            heapq.heappush(maxheap, -q)
            qsum += q # 只用管qsum因为最后的answer一定是用当前最大的ratio去计算的
            if len(maxheap) > K:
                old_q = -heapq.heappop(maxheap)
                qsum -= old_q
            if len(maxheap) == K:
                res = min(res, qsum * cur_ratio)
        
        return res