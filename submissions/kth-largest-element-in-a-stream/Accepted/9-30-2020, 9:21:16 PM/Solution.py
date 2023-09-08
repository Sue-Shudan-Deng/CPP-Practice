// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:
    """
    注意同样是minheap, c++和python的区别
    c++的min在q[-1], python的min在q[0]
    """
    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        for num in nums:
            heapq.heappush(self.q, num)
            if len(self.q) > k:
                heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)