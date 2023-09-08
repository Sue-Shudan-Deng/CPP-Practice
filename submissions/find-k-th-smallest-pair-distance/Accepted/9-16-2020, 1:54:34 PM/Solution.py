// https://leetcode.com/problems/find-k-th-smallest-pair-distance

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = l + (r - l) // 2
            cnt, left = 0, 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > m:
                    left += 1
                cnt += (right - left)
            if cnt >= k:
                r = m
            else:
                l = m + 1
        return l