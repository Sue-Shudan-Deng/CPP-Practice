// https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r - 1 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res