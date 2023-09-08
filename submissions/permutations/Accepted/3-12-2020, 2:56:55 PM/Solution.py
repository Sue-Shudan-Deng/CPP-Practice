// https://leetcode.com/problems/permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def helper(res = [], n = 0):
            if n == len(nums):
                ans.append(res)
                return
            curr = list(filter(lambda x: x not in res, nums))
            for c in curr:
                helper(res + [c], n + 1)
        helper()
        return ans