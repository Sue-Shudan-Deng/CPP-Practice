// https://leetcode.com/problems/strobogrammatic-number-ii

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        mapping = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        numset = [0, 1, 6, 8, 9]
        length = (n + 1) // 2
        res = []
        
        def mirror(res):
            if length % 2 == 0:
                return [r[:-1] + r[-1] + "".join([mapping[i] for i in r[:-1]]) for r in res]
            else:
                return [r + "".join([mapping[i] for i in r]) for r in res]
        
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