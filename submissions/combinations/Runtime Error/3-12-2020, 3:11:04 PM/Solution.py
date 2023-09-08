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
        
        def bt(first = 1, curr = []):
            """
            first 记录从哪个位置开始搜索
            """
            if len(curr) == k:
                ans.append(curr)
            for n in range(first, n + 1):
                curr.append(n) # set
                bt(first + 1, curr)
                curr.pop() # unset
                
        bt()
        return ans