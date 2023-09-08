// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int num = 0;
        
        for( int& integer: nums ){
            int digits = 1;
            while( integer/10 >= 1 ){
                std::cout << integer << std::endl;
                digits++;
                integer = integer/10;
            }
            if( digits%2 == 0 ){
                num++;
            }
        }
    return num;
    }
};