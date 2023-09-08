// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        idxs = list(range(len(s)))
        dict_t = collections.Counter(t)
        cur = dict()
        required = len(dict_t)
        l, r, formed = 0, 0, 0
        ans = (float("inf"), None, None)
        
        while r < len(idxs):
            c = s[r]
            if not cur.get(c):
                cur[c] = 0
            cur[c] += 1
            if cur[c] == dict_t[c]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                c = s[l]
                cur[c] -= 1
                if cur[c] < dict_t[c]:
                    formed -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else "" 