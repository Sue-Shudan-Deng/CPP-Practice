// https://leetcode.com/problems/daily-temperatures

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(), 0);
        stack<pair<int, int>> s;
        for (int i = 0; i < T.size() - 1; ++i) {
            if (T[i] < T[i+1]) {
                res[i] = 1;
                while (!s.empty() && s.top().first < T[i+1]) {
                    auto [t, j] = s.top();
                    s.pop();
                    res[j] = i - j + 1;
                }
            } else {
                s.emplace(T[i], i);
            }
        }
        return res;
    }
};