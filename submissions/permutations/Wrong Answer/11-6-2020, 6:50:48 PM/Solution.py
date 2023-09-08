// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, visited = [], [0 for _ in range(len(nums))]
        def backtrack(start = 1, cur = []):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return 
            for idx in range(len(nums)):
                if not visited[idx]:
                    visited[idx] = 1
                    backtrack(idx + 1, cur + [idx + 1])
                    visited[idx] = 0
                
        backtrack()
        return ans