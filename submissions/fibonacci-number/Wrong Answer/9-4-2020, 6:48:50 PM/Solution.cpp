// https://leetcode.com/problems/fibonacci-number

class Solution {
public:
    int fib(int N) {
        int pre = 0, cur = 1;
        while (N-- > 1) {
            pre = cur;
            cur += pre;
        }
        return cur;
    }
};