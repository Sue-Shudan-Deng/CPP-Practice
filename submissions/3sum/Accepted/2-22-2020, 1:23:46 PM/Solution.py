// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            # 因为i-1已经被看过了，并且i所包含的集合一定是i-1所包含的集合的子集
            # 所以出于duplicate的考虑，不需要考虑i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 之后，固定nums[i]，剩下的变成一个 2 sum 问题
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # 因为nums[i]是unique的，那么去除nums[l]和nums[r]的重复元素
                    while l + 1 < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r - 1 and nums[r] == nums[r-1]:
                        r -= 1
                    # 此时nums[new_l] == nums[l], nums[new_r] == nums[r]
                    # 所以需要继续前进or后退一格
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res