// https://leetcode.com/problems/word-break-ii

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        
        // step1: check if the word is breakable. If not, don't waste time on that
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
        if (!DP.back()) {
            return vector<string>();
        }
        
        vector<vector<string>> DP_(s.size() + 1, vector<string>());
        for (int i = 1; i <= s.size(); ++i) {
            for (auto w : wordDict) {
                auto size = w.size();
                if (i >= size && w == s.substr(i-size, size)) {
                    if (i == size) {
                        DP_[i].push_back(w);
                    } else {
                        for (auto dp : DP_[i-size]) {
                            DP_[i].push_back(dp + " " + w);
                        }
                    }
                }
            }
        }
        return DP_.back();
    }
};