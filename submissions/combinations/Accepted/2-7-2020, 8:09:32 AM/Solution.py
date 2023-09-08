// https://leetcode.com/problems/combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def bt(fst = 1, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return 
            for i in range(fst, n + 1):
                curr.append(i)
                bt(i + 1, curr)
                curr.pop()
        
        bt()
        return res
        