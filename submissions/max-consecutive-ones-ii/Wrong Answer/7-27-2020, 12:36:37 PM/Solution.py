// https://leetcode.com/problems/max-consecutive-ones-ii

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev, curr, res = -1, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prev, curr = curr, 0
            else:
                curr += 1
                res = max(res, prev + curr + 1)
        return res