// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max = 0;
        
        if 1 in nums:
            for i in range(0, len(nums)):

                result = 1
                while i < len(nums)-1 and nums[i] == 1 and nums[i+1] == 1:
                    result += 1
                    i += 1

                if result > max: 
                    max = result
        
        return max

        