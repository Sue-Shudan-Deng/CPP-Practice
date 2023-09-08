// https://leetcode.com/problems/isomorphic-strings

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> m1;
        unordered_map<char, char> m2;
        for (int i = 0; i < s.size(); ++i) {
            char p = s[i];
            char q = t[i];
            if ((m1.count(p) > 0 && m1[p] != q) || (m2.count(q) > 0 && m2[q] != p)) {
                return false;
            }
            m1[p] = q;
            m2[q] = p;
        }
        return true;
    }
};