// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        method 1: 标准解法，非常tricky
        """
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        cur, cnt = 0, 0
        for num in nums:
            cur += num
            cnt += prefix[cur - k] # backward until index -1
            prefix[cur] += 1
            
        return cnt
    
#         """
#         method 2: bianry search
#         """
#         n = len(nums)
#         if n == 0:
#             return 0
#         prefix = [0 for _ in range(n + 1)]
#         prefix[1] = nums[0]
#         for i in range(2, n + 1):
#             prefix[i] = prefix[i-1] + nums[i-1]
            
#         cur, cnt = [[0, 0]], 0
#         for j in range(1, n + 1):
#             l = bisect.bisect_left(cur, [prefix[j] - k])
#             r = bisect.bisect_right(cur, [prefix[j] - k, float("inf")])
#             cnt += (r - l)
#             bisect.insort(cur, [prefix[j], j])
            
#         return cnt