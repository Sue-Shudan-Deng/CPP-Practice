// https://leetcode.com/problems/combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n + 1))
        ans = []
        
        def helper(res = [], cnt = 0):
            if cnt == k:
                ans.append(res)
            curr = list(filter(lambda x: x not in res, nums))
            for c in curr:
                helper(res + [c], cnt + 1)
        
        helper()
        return ans