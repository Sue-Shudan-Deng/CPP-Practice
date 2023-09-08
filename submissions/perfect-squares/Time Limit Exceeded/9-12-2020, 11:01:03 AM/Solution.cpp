// https://leetcode.com/problems/perfect-squares

class Solution {
    
private:
    set<int> squares;
    
public:
    int numSquares(int n) {
        int i = 1, level = 0;
        deque<pair<int, int>> q;
        while (i*i <= n) {
            squares.insert(i*i);
            ++i;
        }
        q.emplace_back(n, level);
        while (!q.empty()) {
            auto [rest, level] = q.front();
            q.pop_front();
            if (rest == 0) {
                return level;
            }
            for (auto i : squares) {
                if (i <= rest) {
                    q.emplace_back(rest-i, level+1);
                }
            }
        }
        return -1;
    }
};