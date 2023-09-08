// https://leetcode.com/problems/word-break-ii

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<vector<string>> DP(s.size() + 1, vector<string>());
        for (int i = 1; i <= s.size(); ++i) {
            for (auto w : wordDict) {
                auto size = w.size();
                if (i >= size && w == s.substr(i-size, size)) {
                    if (i == size) {
                        DP[i].push_back(w);
                    } else {
                        for (auto dp : DP[i-size]) {
                            DP[i].push_back(dp + " " + w);
                        }
                    }
                }
            }
        }
        return DP.back();
    }
};