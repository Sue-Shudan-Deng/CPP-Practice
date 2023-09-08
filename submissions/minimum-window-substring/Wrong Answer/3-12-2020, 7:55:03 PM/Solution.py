// https://leetcode.com/problems/minimum-window-substring

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = collections.Counter(t)
        l, r, formed, curr = 0, 0, 0, dict()
        ans = (float("inf"), l, r)
        while r < len(s):
            char = s[r]
            if not curr.get(char):
                curr[char] = 0
            curr[char] += 1
            if curr[char] == t_dict[char]:
                formed += 1
            while l < r and formed == len(t_dict):
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                curr[s[l]] -= 1
                if curr[s[l]] < t_dict[s[l]]:
                    formed -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else ""
                    