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
        ret *= (fastPow(x, n/2) * fastPow(x, n/2));
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