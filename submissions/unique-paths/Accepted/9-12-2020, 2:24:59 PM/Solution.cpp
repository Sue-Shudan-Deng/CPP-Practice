// https://leetcode.com/problems/unique-paths

class Solution {
    
private:
    map<pair<int, int>, int> mem;
public:
    // recursion with mem
    // int uniquePaths(int m, int n) {
    //     if (m == 0 || n == 0) {
    //         return 0;
    //     }
    //     if (m == 1 && n == 1) {
    //         return 1;
    //     }
    //     if (mem.find(pair<int, int>{m, n}) == mem.end()) {
    //         mem[pair<int, int>{m, n}] = uniquePaths(m-1, n) + uniquePaths(m, n-1);
    //     }
    //     return mem[pair<int, int>{m, n}];
    // }
    
    // DP
    int uniquePaths(int m, int n) {
        vector<vector<int>> DP(m+1, vector<int>(n+1, 0));
        DP[1][1] = 1;
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (!(i == 1 && j == 1)) {
                    DP[i][j] = DP[i-1][j] + DP[i][j-1];    
                }
            }
        }
        return DP[m][n];
    }
};