// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, visited = [], set()
        def backtrack(cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for idx in range(len(nums)):
                if not idx in visited:
                    visited.add(idx)
                    backtrack(cur + [nums[idx]])
                    visited.remove(idx)
                
        backtrack([])
        return ans