// https://leetcode.com/problems/climbing-stairs

class Solution {
private:
    map<int, int> mem;
    
public:
    // Recursion with mem
    int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (mem.find(n) == mem.end()) {
            mem[n] = climbStairs(n-1) + climbStairs(n-2);
        }
        return mem[n];
    }
};
//     // DP
//     int climbStairs(int n) {
//         vector<int> ret(n+1, 1);
//         for (int i = 0; i < n-1; i++) {
//             ret[i+2] = ret[i+1] + ret[i];
//         }
//         return ret[n];
//     }
// };