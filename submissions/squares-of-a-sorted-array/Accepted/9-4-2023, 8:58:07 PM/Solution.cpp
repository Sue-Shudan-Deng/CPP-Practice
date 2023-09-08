// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
        for( int& i: nums){ //notice it should be &, or the vector is not modified
            i = abs(i);
        }
        
        sort(nums.begin(), nums.end());
        
        for( int i: nums){
            std::cout << i << std:: endl;
        }
        
        int size = nums.size();
        vector<int> squared;  //how to set the size of a new vector
        
        for( int i = 0; i < size; i++ ){
            squared.push_back(pow(nums[i],2));
        }
        
        return squared;
        
    }
};