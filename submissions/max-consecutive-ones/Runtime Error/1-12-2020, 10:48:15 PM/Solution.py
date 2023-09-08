// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        快慢指针
        """
        j = 0
        cnt = []
        start = False
        for i in range(len(nums) + 1):
            if i == len(nums) and nums[i - 1] == 1:
                cnt.append(i - j)
                break
            if not start and nums[i] == 1:
                j = i
                start = True
            if start and nums[i] == 1:
                continue
            if start and nums[i] != 1:
                cnt.append(i - j)
                start = False

        return max(cnt) if cnt else 0