// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1] # 左边界
        n, ans = len(heights), 0
        for i in range(n):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                ans = max(ans, heights[index] * (i - stack[-1] - 1))
            stack.append(i)
            
        while stack[-1] != -1:
            index = stack.pop()
            ans = max(ans, heights[index] * (n - stack[-1] - 1))

        return ans