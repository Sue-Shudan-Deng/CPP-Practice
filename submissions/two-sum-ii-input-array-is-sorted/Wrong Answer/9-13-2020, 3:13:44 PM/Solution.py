// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = dict()
        for k, n in enumerate(nums):
            numdict[n] = k
        for k, n in enumerate(nums):
            if target - n in numdict.keys() and k != numdict[target - n]:
                return [k, numdict[target - n]]
        return []
        
        # """
        # sorted版本的twosum可以用一头一尾两个指针来做
        # """
        # lo, hi = 0, len(numbers) - 1
        # while lo < hi:
        #     summ = numbers[lo] + numbers[hi]
        #     if summ < target:
        #         lo += 1
        #     elif summ > target:
        #         hi -= 1
        #     else:
        #         return [lo+1, hi+1]
        # return []