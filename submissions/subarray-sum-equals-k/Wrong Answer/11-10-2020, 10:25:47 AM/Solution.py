// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         """
#         method 1: 标准解法，非常tricky
#         """
#         prefix_sum = collections.defaultdict(int)
#         cursum, cnt = 0, 0
#         for num in nums:
#             cursum += num
#             if cursum == k:
#                 cnt += 1 # forward
#             cnt += prefix_sum[cursum - k] # backward
#             prefix_sum[cursum] += 1
            
#         return cnt
    
        """
        method 2: bianry search
        """
        n = len(nums)
        if n == 0:
            return 0
        prefix = [0 for _ in range(n + 1)]
        prefix[1] = nums[0]
        for i in range(2, n + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
            
        cur, cnt = [[0, 0]], 0
        for j in range(1, n + 1):
            bisect.insort(cur, [prefix[j], j])
            print(cur, j, prefix[j] - k)
            l = bisect.bisect_left(cur, [prefix[j] - k])
            r = bisect.bisect_right(cur, [prefix[j] - k, float("inf")])
            if r == len(cur):
                r -= 1
            cnt += (r - l)
            
        return cnt