// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(op: str, num1: int, num2: int) -> int:
            if op == '+':
                return int(num1) + int(num2)
            if op == '-':
                return int(num1) - int(num2)
            if op == '*':
                return int(float(num1) * float(num2))
            if op == '/':
                return int(float(num1) / float(num2))
            
        stack = []
        ops = ['+', '-', '*', '/']
        res = 0
        for t in tokens:
            if t not in ops:
                stack.append(t)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(eval(t, num1, num2))
        return stack[-1]