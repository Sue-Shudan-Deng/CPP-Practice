// https://leetcode.com/problems/isomorphic-strings

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> m;
        for (int i = 0; i < s.size(); ++i) {
            char p = s[i];
            char q = t[i];
            if (m.count(p) > 0 && m[p] != q) {
                return false;
            }
            m[p] = q;
        }
        return true;
    }
};