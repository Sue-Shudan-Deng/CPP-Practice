// https://leetcode.com/problems/3sum-closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = float("inf")
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            l, r = i + 1, length - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                if abs(ans - target) > abs(nums[i] + nums[l] + nums[r] - target):
                    ans = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans