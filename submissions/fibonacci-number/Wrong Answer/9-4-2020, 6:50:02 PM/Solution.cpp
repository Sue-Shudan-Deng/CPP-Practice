// https://leetcode.com/problems/fibonacci-number

class Solution {
public:
    int fib(int N) {
        int pre = 0, cur = 1, ret = 0;
        while (N-- > 1) {
            ret = pre + cur;
            pre = cur;
            cur = ret;
        }
        return ret;
    }
};