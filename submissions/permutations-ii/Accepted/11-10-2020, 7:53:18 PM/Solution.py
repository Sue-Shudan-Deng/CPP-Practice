// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, visited = [], set()
        def backtrack(cur):
            n = len(nums)
            
            if len(cur) == n:
                ans.append(cur)
            
            for i in range(n):
                if i in visited:
                    continue
                visited.add(i)
                backtrack(cur + [nums[i]])
                visited.remove(i)
                
        backtrack([])
        return list(set([tuple(i) for i in ans]))