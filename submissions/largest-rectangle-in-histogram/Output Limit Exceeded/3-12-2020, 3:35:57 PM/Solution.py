// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxnum = 0
        n = len(heights)
        
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxnum = max(maxnum, heights[stack.pop()] * (i-stack[-1]-1))
            stack.append(i)
            print(i, stack)
        
        while stack[-1] != -1:
            maxnum = max(maxnum, heights[stack.pop()] * (n-stack[-1]-1))
            
        return maxnum