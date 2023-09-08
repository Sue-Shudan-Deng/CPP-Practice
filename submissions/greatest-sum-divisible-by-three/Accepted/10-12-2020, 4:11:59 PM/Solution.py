// https://leetcode.com/problems/greatest-sum-divisible-by-three

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # """
        # Target sum, TLE, O(mn) ~ 10^8
        # """
        # summ = sum(nums)
        # if summ % 3 == 0:
        #     return summ
        # nums.sort()
        # dp = [False for _ in range(summ + 1)]
        # dp[0] = True
        # for num in nums:
        #     for i in range(summ, num - 1, -1):
        #         dp[i] = dp[i] or dp[i-num]
        # for j in range(summ, -1, -1):
        #     if j % 3 == 0 and dp[j]:
        #         break
        # return j
        """
        method 2, 太巧妙，O(m), https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space
        """
        seen = [0, 0, 0]
        for num in nums:
            for i in seen[:]:
                seen[(i + num) % 3] = max(seen[(i + num) % 3], i + num)
        return seen[0]