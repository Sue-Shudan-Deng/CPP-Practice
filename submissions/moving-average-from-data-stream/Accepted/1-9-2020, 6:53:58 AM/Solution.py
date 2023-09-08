// https://leetcode.com/problems/moving-average-from-data-stream

from collections import deque    
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.count = 0
        self.window_sum = 0
        
    def next(self, val: int) -> float:
        
        if self.count == self.size:
            tail = self.queue.popleft()
            self.count -= 1
            self.window_sum -= tail
        self.queue.append(val)
        self.window_sum += val
        self.count += 1
        return self.window_sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)