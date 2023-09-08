// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, visited = [], collections.defaultdict(int)
        def backtrack(cur = []):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return 
            for idx in range(len(nums)):
                if not visited[idx]:
                    visited[idx] = 1
                    backtrack(cur + [nums[idx]])
                    visited[idx] = 0
                
        backtrack()
        return ans