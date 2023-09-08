// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = collections.defaultdict(int)
        cursum, cnt = 0, 0
        for num in nums:
            cursum += num
            if cursum == k:
                cnt += 1
            cnt += h[cursum - k]
            h[cursum] += 1
            
        return cnt