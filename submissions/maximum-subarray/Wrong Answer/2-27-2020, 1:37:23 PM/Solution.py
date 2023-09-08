// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def crossSum(left, right, p):
            if left == right:
                return nums[left]
            leftsum, currsum = float("-inf"), 0
            for i in range(p, left - 1, -1):
                currsum += nums[i]
                leftsum = max(leftsum, currsum)
            rightsum, currsum = float("-inf"), 0
            for i in range(p + 1, right, 1):
                currsum += nums[i]
                rightsum = max(rightsum, currsum)
            return leftsum + rightsum
        def helper(left, right):
            if left == right:
                return nums[left]
            p = (left + right) // 2
            leftsum = helper(left, p)
            rightsum = helper(p + 1, right)
            crosssum = crossSum(left, right, p)
            return max(leftsum, rightsum, crosssum)
        return helper(0, len(nums) - 1)