// https://leetcode.com/problems/product-of-array-except-self

# O(n)
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
    
# O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left and right array
        # 首先, left直接就是ans的一部分
        # 其次，R没必要写成list形式
        ans = [1] * len(nums)
        for k in range(1, len(nums)):
            ans[k] = ans[k-1] * nums[k-1]
        R = 1
        for k in range(len(nums) - 1, -1, -1):
            ans[k] *= R
            R *= nums[k]
        return ans