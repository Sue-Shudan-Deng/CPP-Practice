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
        for num in nums:
            l, r = 0, size
            while l < r:
                m = l + (r - l) // 2
                if tails[m] >= num:
                    r = m
                else:
                    l = m + 1
            tails[l] = num
            size = max(l + 1, size)
        return size