// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getResult(S: str):
            cnt, res = 0, ""
            S = S[::-1]
            for s in S:
                if s == '#':
                    cnt += 1
                else:
                    if not cnt:
                        res += s
                    else:
                        cnt -= 1
            return res[::-1]
        
        return getResult(S) == getResult(T)