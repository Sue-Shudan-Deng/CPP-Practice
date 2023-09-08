// https://leetcode.com/problems/minimum-window-substring

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = collections.Counter(t)
        length = len(s)
        required = len(t_dict)
        cur = dict()
        l, r, formed = 0, 0, 0
        ans = (float("inf"), l, r)
        while r < length:
            c = s[r]
            if not cur.get(c):
                cur[c] = 0
            cur[c] += 1
            if cur[c] == t_dict[c]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                c = s[l]
                cur[c] -= 1
                if cur[c] < t_dict[c]:
                    formed -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else ""