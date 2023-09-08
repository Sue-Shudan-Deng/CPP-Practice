// https://leetcode.com/problems/climbing-stairs

class Solution {
public:
    int climbStairs(int n) {
        vector<int> ret(n+1);
        fill(ret.begin(), ret.end(), 1);
        for (int i = 0; i < n-1; i++) {
            ret[i+2] = ret[i+1] + ret[i];
        }
        return ret[n];
    }
};