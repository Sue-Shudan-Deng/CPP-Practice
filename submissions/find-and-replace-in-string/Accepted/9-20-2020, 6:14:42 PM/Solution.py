// https://leetcode.com/problems/find-and-replace-in-string

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        if len(indexes) == 0:
            return S
        
        x = list(zip(indexes, sources))
        x.sort(key = lambda a: a[0])
        y = list(zip(indexes, targets))
        y.sort(key = lambda a: a[0])        
        cur, n, n1 = 0, len(indexes), len(S)
        for i in range(0, n):
            if S[x[i][0]:x[i][0]+len(x[i][1])] == x[i][1]:
                if cur < x[i][0]:
                    res += S[cur:x[i][0]]
                    cur = x[i][0]
                res += y[i][1]
                cur += len(x[i][1])
        if cur < n1:
            res += S[cur:n1]
        return res