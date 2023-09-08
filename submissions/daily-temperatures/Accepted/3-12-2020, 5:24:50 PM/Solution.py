// https://leetcode.com/problems/daily-temperatures

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(T))]
        stack = []
        
        for i in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res