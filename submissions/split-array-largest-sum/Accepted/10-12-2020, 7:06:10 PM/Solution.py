// https://leetcode.com/problems/split-array-largest-sum

class Solution:
    
    # # method 1: DP: TLE
    # def splitArray(self, nums: List[int], m: int) -> int:
    #     n = len(nums)
    #     dp = [[float("inf") for j in range(n+1)] for i in range(m+1)]
    #     prefix = [0 for _ in range(n+1)]
    #     for i in range(1, n+1):
    #         prefix[i] = prefix[i-1] + nums[i-1]
    #     dp[0][0] = 0
    #     for k in range(1, m+1):
    #         for i in range(1, n+1):
    #             for j in range(i):
    #                 dp[k][i] = min(dp[k][i], max(dp[k-1][j], (prefix[i]-prefix[j])))
    #     return dp[-1][-1]
    
    # method 2: Binary search
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        ans = r
        while l < r:
            # calculate cnt
            m = l + (r - l) // 2
            summ = 0
            cnt = 1
            # how to calculate cnt
            # 因为这里是最紧凑的计数方式，所以相当于算的是所有可能的subarray的总数的最大值
            for n in nums:
                if summ + n > m:
                    cnt += 1
                    summ = n
                else:
                    summ += n
            if cnt <= k:
                # 再往左走没有意义，因为cnt只会越来越小
                ans = min(ans, m)
                r = m
            else:
                l = m + 1
        return ans