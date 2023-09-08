// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]
        prefix[1] = nums[0]
        for i in range(2, n + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
            
        cur, ans = [[0, 0]], 0
        for j in range(1, n + 1):
            bisect.insort(cur, [prefix[j], j])
            p = bisect.bisect_left(cur, [prefix[j] - k])
            if p < len(cur) and prefix[j] - cur[p][0] == k:
                ans = max(ans, j - cur[p][1])
            
        return ans