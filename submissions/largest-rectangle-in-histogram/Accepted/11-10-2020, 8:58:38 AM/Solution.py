// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        monotonic stack
        """
        
        stack = [-1] # 左边界
        n, ans = len(heights), 0
        for i in range(n):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                ans = max(ans, heights[index] * (i - stack[-1] - 1)) # 右边界 - 左边界
            stack.append(i)
            
        while stack[-1] != -1:
            index = stack.pop()
            ans = max(ans, heights[index] * (n - stack[-1] - 1)) # 右边界 - 左边界

        return ans