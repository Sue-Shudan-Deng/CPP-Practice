// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            # 退出条件：l = r
            m = l + (r - l) // 2
            if isBadVersion(m):
                # 满足该条件的第一个
                r = m
            else:
                l = m + 1
        return l