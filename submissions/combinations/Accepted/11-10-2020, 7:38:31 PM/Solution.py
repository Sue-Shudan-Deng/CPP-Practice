// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start: int, ans: List[int]):
            if len(ans) == k:
                res.append(ans[:])
                return
            for i in range(start, n + 1):
                backtrack(i+1, ans + [i]) # 回溯
        backtrack(1, [])
        return res
