// https://leetcode.com/problems/3sum-closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                if abs(nums[i] + nums[l] + nums[r] - target) < abs(ans - target):
                    ans = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > target:
                    r -= 1
        return ans
            