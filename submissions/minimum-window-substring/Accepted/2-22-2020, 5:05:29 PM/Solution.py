// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = dict()
        for i, ch in enumerate(s):
            if ch in t:
                s_dict[i] = ch
        idxs = list(s_dict.keys())
        dict_t = collections.Counter(t)
        cur = dict()
        required = len(dict_t)
        l, r, formed = 0, 0, 0
        ans = (float("inf"), None, None)
        
        while r < len(idxs):
            ch = s_dict[idxs[r]]
            if not cur.get(ch):
                cur[ch] = 0
            cur[ch] += 1
            if cur[ch] == dict_t[ch]:
                formed += 1
            # print("out", l, r, ch, formed)
            while l <= r and formed == required:
                start = idxs[l]
                end = idxs[r]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                ch = s_dict[start]
                cur[ch] -= 1
                if cur[ch] < dict_t[ch]:
                    formed -= 1
                # print("in", l, r, ch, formed)
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1] if ans[0] != float("inf") else "" 