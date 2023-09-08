// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        def backtrack(first, length, cur):
            if len(cur) == length:
                ans.append(cur[:])
                return
            for i in range(first, n):
                backtrack(i + 1, length, cur + [nums[i]])
        
        for k in range(n + 1):
            backtrack(0, k, [])
        return ans