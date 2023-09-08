// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = collections.Counter(t)
        l, r, formed, cnt = 0, 0, 0, collections.defaultdict(int)
        ans = (float("inf"), l, r)
        while r < len(s):
            c = s[r]
            cnt[c] += 1
            if cnt[c] == t[c]:
                formed += 1
            while l <= r and formed == len(t):
                ans = min(ans, (r-l+1, l, r), key = lambda x:x[0])
                c = s[l]
                cnt[c] -= 1
                if cnt[c] < t[c]:
                    formed -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else ""