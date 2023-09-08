// https://leetcode.com/problems/number-of-longest-increasing-subsequence

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        可以转换成300. Longest Increasing Subsequence + 计数dp
        需要特别理解[2,2,2,2,2]这个case
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)] # dp[i] 包含index i后能达到的最大长度为多少
        count = [1 for _ in range(n)] # 包含index i的当前最大长度下，最多有多少个
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # 为了达到最大，不断更新
                    # 一旦达到最大，开始累积
                    if dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    dp[i] = max(dp[i], dp[j] + 1)
        longest = max(dp)
        return sum([c for i, c in enumerate(count) if dp[i] == longest])