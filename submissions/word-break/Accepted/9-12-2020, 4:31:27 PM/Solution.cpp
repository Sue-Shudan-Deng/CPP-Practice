// https://leetcode.com/problems/word-break

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> DP(s.size() + 1, false);
        DP[0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            for (auto w : wordDict) {
                auto size = w.size();
                if (i >= size) {
                    DP[i] = DP[i] || (DP[i-size] && w == s.substr(i-size, size));
                }
            }
        }
        return DP.back();
    }
};