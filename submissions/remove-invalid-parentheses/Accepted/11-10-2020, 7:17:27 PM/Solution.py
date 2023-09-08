// https://leetcode.com/problems/remove-invalid-parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for i in s:
                if i == "(":
                    cnt += 1
                elif i == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0
        
        ans = []
        def dfs(s, start, l, r):
            n = len(s)
            if l == 0 and r == 0 and isValid(s):
                ans.append(s)
                
            for i in range(start, n):
                ch = s[i]
                if not (ch == "(" or ch == ")"):
                    continue
                    
                if i != start and s[i] == s[i-1]:
                    continue
                
                # 因为这里 l == 0 and r == 0 不满足，所以必然会删除一个                
                new_s = s[:i] + s[i+1:]
                # step 1: remove ")" before "("
                if s[i] == ")" and r > 0:
                    dfs(new_s, i, l, r - 1)
                    
                if s[i] == "(" and l > 0:
                    dfs(new_s, i, l - 1, r)
                    
        l, r = 0, 0
        for c in s:
            l += (c == "(")
            if l == 0:
                r += (c == ")")
            else:
                l -= (c == ")")
        
        dfs(s, 0, l ,r)
        return ans if ans else [""]