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
                # 如果当前值是true，那么一定不能向右了，那么就守在这里
                r = m
            else:
                # 如果当前值是false，那么一定不能向左了，并且向右移动一位
                l = m + 1
        return l