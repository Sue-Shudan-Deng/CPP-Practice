// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int cnt = 0, n = s.size();
        map<int, int> visited;
        int l = 0, r = 0;
        int res = 2;
        if (n < 3) {
            return n;
        }
        while (r < n) {
            if (visited.size() < 3) {
                visited[s[r]] = r;
                ++r;
            }
            if (visited.size() == 3) {
                auto [key, index] = *min_element(visited.begin(), visited.end(), [](auto x, auto y) {return x.second < y.second;}); // 这一步真是太妙了，学习了
                visited.erase(s[index]);
                l = index + 1;
            }
            res = max(res, r - l);
        }
        return res;
    }
};