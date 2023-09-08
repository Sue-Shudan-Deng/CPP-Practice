// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numdict = dict()
        # for k, n in enumerate(nums):
        #     numdict[n] = k
        # for k, n in enumerate(nums):
        #     if target - n in numdict.keys() and k != numdict[target - n]:
        #         return [k+1, numdict[target - n]+1]
        # return []
        
        """
        这里unsorted版本的代码也是完全适用的，
        只不过sorted版本的twosum也可以首尾双指针来做
        """
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            summ = numbers[lo] + numbers[hi]
            if summ < target:
                lo += 1
            elif summ > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
        return []