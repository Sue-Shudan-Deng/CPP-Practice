// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0, j = 0, ans = 0;
        int n = s.size();
        set<char> visited;
        
        while (i < n && j < n) {
            if (visited.count(s[j]) == 0) {
                visited.insert(s[j++]);
                ans = max(ans, j-i);
            } else {
                visited.erase(s[i--]);
            }
        }
        return ans;
    }
};