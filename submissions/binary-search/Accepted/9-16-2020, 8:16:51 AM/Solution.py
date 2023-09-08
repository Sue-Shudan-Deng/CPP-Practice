// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            # 需要依靠l=r来确保收敛
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # End Condition: left > right
        return -1    