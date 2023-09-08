// https://leetcode.com/problems/word-break

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> wordDict_ = set<string>(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            for (auto w : wordDict_) {
                auto size = w.size();
                if (i >= size && w == s.substr(i-size, size)) {
                    dp[i] = dp[i] || dp[i-size];
                }
            }
        }
        return dp.back();
    }
};