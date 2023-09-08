// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = dict()
        for k, n in enumerate(nums):
            numdict[n] = k
        for k, n in enumerate(nums):
            if target - n in numdict and k != numdict[n]:
                return [k, numdict[n]]
        return []