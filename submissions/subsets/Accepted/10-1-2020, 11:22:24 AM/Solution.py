// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(first, length, cur, ans):
            if len(cur) == length:
                ans.append(cur[:])
                return
            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i + 1, length, cur, ans)
                cur.pop()
            
        ans = []
        for k in range(n + 1):
            backtrack(0, k, [], ans)
        return ans