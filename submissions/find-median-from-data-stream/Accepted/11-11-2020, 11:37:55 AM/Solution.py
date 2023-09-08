// https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:
    """
    这个解法太巧妙了
    """
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

        # len(self.large) == len(self.small) or 
        # len(self.large) == len(self.small) + 1
        
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -num)
            largest_in_small = -heapq.heappop(self.small)
            heapq.heappush(self.large, largest_in_small)
        else:
            heapq.heappush(self.large, num)
            smallest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_in_large)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()