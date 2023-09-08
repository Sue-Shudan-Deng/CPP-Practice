// https://leetcode.com/problems/number-of-longest-increasing-subsequence

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        可以转换成300. Longest Increasing Subsequence + 纯粹的计数
        需要特别理解[2,2,2,2,2]这个case
        """
        n = len(nums)
        if n == 0:
            return 0
        dp, count = [1 for _ in range(n)], [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    """
                    这道题的难点在于下面这几行
                    如何只在dp[i]最大的时候计数
                    """
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]: # 表示已经达到当前最大值了
                        count[i] += count[j]
        
        longest = max(dp)
        return sum([c for i, c in enumerate(count) if dp[i] == longest])
        