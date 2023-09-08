// https://leetcode.com/problems/edit-distance

class Solution {
public:
    int minDistance(string word1, string word2) {
        if (word1.size() == 0 || word2.size() == 0) {
            return word1.size() + word2.size();
        }
        vector<vector<int>> DP(word1.size() + 1, vector<int>(word2.size() + 1, 0));
        for (int i = 0; i <= word1.size(); ++i) {
            DP[i][0] = i;
        }
        
        for (int j = 0; j <= word2.size(); ++j) {
            DP[0][j] = j;
        }
        
        for (int i = 1; i <= word1.size(); ++i) {
            for (int j = 1; j <= word2.size(); ++j) {
                if (word1[i-1] == word2[j-1]) {
                    DP[i][j] = min(min(DP[i][j-1] + 1, DP[i-1][j] + 1), DP[i-1][j-1]);
                } else {
                    DP[i][j] = min(min(DP[i][j-1] + 1, DP[i-1][j] + 1), DP[i-1][j-1] + 1);
                }
                
            }
        }
        return DP.back().back();
    }
};