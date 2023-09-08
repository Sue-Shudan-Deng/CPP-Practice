// https://leetcode.com/problems/daily-temperatures

class Solution:
    # 注：这里的思路是，逆序，并且对于每个T用栈只保留递次增加的t
    # 难题！！！务必反复看解析
    # 逆向单调栈
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0 for _ in range(n)] 
        stack = []
        for i in range(n-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res