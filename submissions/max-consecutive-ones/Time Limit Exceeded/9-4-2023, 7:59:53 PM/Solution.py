// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max = 1;
        sum = 0;
        
        for i in range(0, len(nums)):
            sum += nums[i]
            
            result = 1
            while i < len(nums)-1 and nums[i] == 1 and nums[i+1] == 1:
                result += 1
                i += 1
            
            
            if result > max: 
                max = result
            
        
        
        if sum == 0 or len(nums) == 0: 
            max = 0
        
        
        return max

        