// https://leetcode.com/problems/perfect-squares

class Solution {
    
// private:
//     set<int> squares;
    
// public:
// Time Limit Exceeds
//     int numSquares(int n) {
//         int i = 1, level = 0;
//         deque<pair<int, int>> q;
//         while (i*i <= n) {
//             squares.insert(i*i);
//             ++i;
//         }
//         q.emplace_back(n, level);
//         while (!q.empty()) {
//             auto [rest, level] = q.front();
//             q.pop_front();
//             if (rest == 0) {
//                 return level;
//             }
//             for (auto i : squares) {
//                 if (i <= rest) {
//                     q.emplace_back(rest-i, level+1);
//                 }
//             }
//         }
//         return -1;
//     }
// };
    
public:
    int numSquares(int n) {
        int i = 1, level = 0;
        set<int> squares;
        deque<pair<int, int>> q;
        while (i*i <= n) {
            squares.insert(i*i);
            ++i;
        }
        
        vector<int>dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (auto s : squares) {
            for (int i = 0; i <= n; ++i) {
                if (i >= s) {
                    dp[i] = min(dp[i], dp[i-s] + 1);
                }
            }
        }
        return dp[n];
    }
};