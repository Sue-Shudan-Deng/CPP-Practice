// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        用deque
        """
        def clean_deque(i):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
        # initialize
        queue = collections.deque()
        max_idx = 0
        output = []
        
        for i in range(k):
            clean_deque(i)
            queue.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output.append(nums[max_idx])
        
        for i in range(k, len(nums)):
            clean_deque(i)
            queue.append(i)
            output.append(nums[queue[0]])
        
        return output