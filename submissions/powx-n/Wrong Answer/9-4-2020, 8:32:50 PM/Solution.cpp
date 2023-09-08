// https://leetcode.com/problems/powx-n

// recursion
class Solution {
    
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        double ret = 1;
        if (n % 2) {
            ret *= n < 0 ? x : 1/x;  //这里还挺巧妙的
        }
        double half = myPow(x, n/2);
        ret *=  half * half;
        return ret;
    }
};