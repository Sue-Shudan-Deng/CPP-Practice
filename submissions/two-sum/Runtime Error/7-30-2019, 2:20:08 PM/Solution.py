// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = list()
        for a, i in enumerate(nums):
            if target - i in nums:
                b = nums.index(target - i)
                p.append((a,b))
        p = list(filter(lambda x: x[0]!=x[1] and x[0] < x[1], p))[0]
        return p
        