// https://leetcode.com/problems/find-and-replace-in-string

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        if len(indexes) == 0:
            return S
        cur, n, n1 = 0, len(indexes), len(S)
        for i in range(0, n):
            if S[indexes[i]:indexes[i]+len(sources[i])] == sources[i]:
                if cur < indexes[i]:
                    res += S[cur:indexes[i]]
                    cur = indexes[i]
                res += targets[i]
                cur += len(sources[i])
        if cur < n1:
            res += S[cur:n1]
        return res