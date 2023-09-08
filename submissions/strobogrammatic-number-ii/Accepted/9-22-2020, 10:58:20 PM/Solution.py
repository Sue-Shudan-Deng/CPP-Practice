// https://leetcode.com/problems/strobogrammatic-number-ii

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        mapping = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        numset = [0, 1, 6, 8, 9]
        numset2 = [0, 1, 8]
        length = n // 2
        res = []
        
        def transform(r):
            return "".join([mapping[i] for i in r][::-1])
        
        def mirror(res):
            if n % 2 == 1:
                return [r + str(i) + transform(r) for i in numset2 for r in res]
            else:
                return [r + transform(r) for r in res]
        
        def dfs(cur, res):
            if len(cur) == length:
                res.append(cur)
                return
            for n in numset:
                if cur == "" and n == 0:
                    continue
                cur += str(n)
                dfs(cur, res)
                cur = cur[:-1]
                
        dfs("", res)
        return mirror(res)