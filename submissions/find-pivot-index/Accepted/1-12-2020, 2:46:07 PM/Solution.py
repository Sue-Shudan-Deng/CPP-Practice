// https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        leftsum = 0
        for k, n in enumerate(nums):
            if leftsum == summ - leftsum - n:
                return k
            leftsum += n
        return -1