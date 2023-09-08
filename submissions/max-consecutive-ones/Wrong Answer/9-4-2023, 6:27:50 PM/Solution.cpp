// https://leetcode.com/problems/max-consecutive-ones

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0;
        
        for( int i = 0; i < nums.size()-1; i++){
            
            int result = 1;
            while( nums[i] == 1 && nums[i+1] == 1 ){
                result++;
                i++;
            }
            
            if( result > max){
                max = result;
            }
        }
        
        int sum = 0;
        for( int i: nums){
            sum += i;
        }
        if( sum == 0 ){
            max = 0;
        }
        
        return max;
    }
};