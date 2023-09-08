// https://leetcode.com/problems/minimum-window-substring

class Solution {
public:
    string minWindow(string s, string t) {
        map<char, int> counter;
        for (auto i : t) {
            if (!counter.count(i)) {
                counter[i] = 0;
            }
            ++counter[i];
        }
        int l = 0, r = 0, formed = 0;
        int n = s.size();
        map<char, int> cur;
        tuple<int, int, int> ans{INT_MAX, l, r}; 
        char k;
        while (r < n) {
            k = s[r];
            ++cur[k];
            if (counter.count(k) && cur[k] == counter[k]) {
                ++formed;
            }
            while (l <= r && formed == counter.size()) {
                if (r-l+1 < get<0>(ans)) {
                    ans = make_tuple(r-l+1, l, r);
                }
                k = s[l];
                --cur[k];
                if (counter.count(k) && cur[k] < counter[k]) {
                    --formed;
                }
                ++l;
            }
            ++r;
        }
        return get<0>(ans) < INT_MAX ? s.substr(get<1>(ans), get<0>(ans)) : "";
    }
};