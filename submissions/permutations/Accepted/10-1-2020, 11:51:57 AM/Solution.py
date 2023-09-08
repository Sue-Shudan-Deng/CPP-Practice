// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(res = [], n = 0):
            if n == len(nums):
                ans.append(res)
                return 
            curr = list(filter(lambda x: not x in res, nums))
            for i in curr:
                backtrack(res + [i], n + 1)
                
        backtrack()
        return ans