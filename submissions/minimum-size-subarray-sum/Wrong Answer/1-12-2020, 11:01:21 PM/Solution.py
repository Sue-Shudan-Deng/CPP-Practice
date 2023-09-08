// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        先考虑双指针
        """
        i = 0
        ans = sys.maxsize
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            while (summ >= s):
                ans = min(ans, j - i + 1)
                summ -= nums[i] # 只减去左边那个元素
                i += 1
        return ans  