// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left and right array
        L, R = [1] * len(nums), [1] * len(nums)
        ans = [0] * len(nums)
        for k in range(1, len(nums)):
            L[k] = L[k-1] * nums[k-1]
        for k in range(len(nums) - 2, -1, -1):
            R[k] = R[k+1] * nums[k+1]
        for k in range(len(nums)):
            ans[k] = L[k] * R[k]
        return ans