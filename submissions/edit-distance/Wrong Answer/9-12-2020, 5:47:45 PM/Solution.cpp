// https://leetcode.com/problems/edit-distance

class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> DP(word1.size() + 1, vector<int>(word2.size() + 1, 0));
        for (int i = 1; i <= word1.size(); ++i) {
            for (int j = 1; j <= word2.size(); ++j) {
                DP[i][j] = min(min(DP[i][j-1] + 1, DP[i-1][j] + 1), DP[i-1][j-1] + 1);
            }
        }
        return DP.back().back();
    }
};