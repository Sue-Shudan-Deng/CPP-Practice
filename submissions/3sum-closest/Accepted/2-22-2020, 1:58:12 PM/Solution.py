// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[-1]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                if abs(nums[i] + nums[l] + nums[r] - target) < abs(ans - target):
                    ans = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans