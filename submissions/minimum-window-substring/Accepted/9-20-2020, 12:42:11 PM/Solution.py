// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = collections.Counter(t)
        l, r, formed, cur = 0, 0, 0, dict()
        ans = (float("inf"), l, r)
        while r < len(s):
            c = s[r]
            if not cur.get(c):
                cur[c] = 0
            cur[c] += 1
            if cur[c] == t_dict[c]:
                formed += 1
            while l <= r and formed == len(t_dict):
                ans = min(ans, (r-l+1, l, r), key = lambda x:x[0])
                c = s[l]
                cur[c] -= 1
                if cur[c] < t_dict[c]:
                    formed -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else ""