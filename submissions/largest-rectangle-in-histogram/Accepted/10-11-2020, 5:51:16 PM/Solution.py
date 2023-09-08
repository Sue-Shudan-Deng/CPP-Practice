// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        C++的写法要更清晰一点
        """
        stack = [-1]
        maxnum = 0
        n = len(heights)
        
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                x = heights[stack.pop()]
                x *= (i-stack[-1]-1)
                maxnum = max(maxnum, x)
            stack.append(i)
        
        while stack[-1] != -1:
            x = heights[stack.pop()]
            x *= (n-stack[-1]-1)
            maxnum = max(maxnum, x)
            
        return maxnum