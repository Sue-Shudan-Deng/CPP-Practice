// https://leetcode.com/problems/happy-number

class Solution {
    
private:
    int getNumsSquares(int x) {
        int cnt = 0;
        while (x) {
            cnt += pow(x % 10, 2);
            x /= 10;
        }
        return cnt;
    }
    
public:
    bool isHappy(int n) {
        set<int> s;
        while (n != 1) {
            if (s.count(n) > 0) {
                return false;
            }
            s.insert(n);
            n = getNumsSquares(n);
        }
        return true;
    }
};