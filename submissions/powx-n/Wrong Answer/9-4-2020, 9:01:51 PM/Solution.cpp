// https://leetcode.com/problems/powx-n

// // recursion
// class Solution {
    
// public:
//     double myPow(double x, int n) {
//         if (n == 0) return 1;
//         double ret = 1;
//         if (n % 2) {
//             ret *= n < 0 ? 1/x : x;  //这里还挺巧妙的
//         }
//         double half = myPow(x, n/2);
//         ret *=  half * half;
//         return ret;
//     }
// };

// iteration
class Solution {
    
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        vector<int> breaking;
        while (n > 0) {
            n /= 2;
            breaking.push_back(n);
        }
        double cur = n < 0 ? 1/x : x;
        double ret = 1;
        for (auto i : breaking) {
            if (i % 2) ret *= n < 0 ? 1/x : x;
            ret *= (cur * cur);
        }
        return ret;
    }
};