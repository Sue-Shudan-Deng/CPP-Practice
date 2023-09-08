// https://leetcode.com/problems/fibonacci-number

class Solution {
public:
    int fib(int N) {
        int pre1 = 0, pre2 = 1;
        int cur = (N == 0 ? 0 : 1);
        while (N-- > 1) {
            cur = pre1 + pre2;
            pre1 = pre2;
            pre2 = cur;
        }
        return cur;
    }
};