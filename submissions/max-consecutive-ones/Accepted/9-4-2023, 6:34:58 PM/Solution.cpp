// https://leetcode.com/problems/max-consecutive-ones

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 1;
        int sum = 0;
        
        for( int i = 0; i < nums.size(); i++){
            sum += nums[i];
            
            int result = 1;
            while( i < nums.size()-1 && nums[i] == 1 && nums[i+1] == 1 ){
                result++;
                i++;
            }
            
            if( result > max){
                max = result;
            }
        }
        
        
        if( sum == 0 | nums.empty()){
            max = 0;
        }
        
        return max;
    }
};