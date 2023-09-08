// https://leetcode.com/problems/powx-n

// recursion
class Solution {
    
private:
    double fastPow(double x, int n) {
        if (n == 0) return 1;
        double ret = 1;
        if (n % 2 == 1) {
            ret *= x;
        }
        double half = fastPow(x, n/2);
        ret *=  half * half;
        return ret;
    }
    
public:
    double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        return fastPow(x, n);
    }
};