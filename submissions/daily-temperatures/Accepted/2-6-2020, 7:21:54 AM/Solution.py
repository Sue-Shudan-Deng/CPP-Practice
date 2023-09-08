// https://leetcode.com/problems/daily-temperatures

class Solution:
    # 注：这里的思路是，逆序，并且对于每个T用栈只保留递次增加的t
    # 难题！！！务必反复看解析
    # 这道题相当于说，stack栈底的元素存储较远的更大值(更大)，栈顶的元素
    # 存储较近的更大值(稍大)，这样每次pop出来就能检索到离得最近的更大值
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res