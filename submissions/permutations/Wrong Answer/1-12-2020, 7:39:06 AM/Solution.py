// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(res = [], n = 0):
            if n > len(nums):
                return
            if n == 3:
                ans.append(res)
                return 
            curr = list(filter(lambda x: not x in res, nums))
            for i in curr:
                helper(res + [i], n + 1)
                
        helper()
        return ans