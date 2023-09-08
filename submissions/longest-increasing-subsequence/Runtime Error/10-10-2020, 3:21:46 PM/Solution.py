// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # """
        # method 1: DP: O(n^2)
        # """
        # n = len(nums)
        # if n == 0:
        #     return 0
        # dp = [1 for _ in range(n)]
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)
    
        """
        method 2: DP + Binary Search: O(nlog(n))
        https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)