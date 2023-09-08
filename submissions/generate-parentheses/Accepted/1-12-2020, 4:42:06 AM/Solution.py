// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        普通递归
        """
        ans = set()
        def backtrack(S = '', left = 0, right = 0):
            """
            S是当前字符串, left是左括号个数, right是右括号个数
            """
            if left > n or right > n:
                return
            if left == n and right == n:
                ans.add(S)
            
            # 只有当left < n才有添加左括号的必要
            if left < n:
                backtrack(S +'(', left + 1, right)
            # 只有当right < left才有添加右括号的必要
            if right < left:
                backtrack(S +')', left, right + 1)
        
        backtrack()
        return list(ans)

    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        stack代替递归
        """
        ans = set()
        S = ''
        left = 0
        right = 0
        stack = [(S, left, right)]
        while stack:
            S, left, right = stack.pop()
            if left > n or right > n:
                continue
            if left == n and right == n:
                ans.add(S)
            
            if left < n:
                stack.append((S +'(', left + 1, right))
            if right < left:
                stack.append((S +')', left, right + 1))
            
        return list(ans)