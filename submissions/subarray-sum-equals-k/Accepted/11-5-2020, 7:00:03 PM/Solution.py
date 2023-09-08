// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = collections.defaultdict(int)
        cursum, cnt = 0, 0
        for num in nums:
            cursum += num
            if cursum == k:
                cnt += 1 # forward
            cnt += prefix_sum[cursum - k] # backward
            prefix_sum[cursum] += 1
            
        return cnt