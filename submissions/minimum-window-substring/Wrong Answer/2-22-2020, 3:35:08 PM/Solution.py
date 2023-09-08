// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = (len(s), s)
        if len(s) == len(t):
            return s if s == t else ""
        for i in range(len(s) - len(t)):
            new_t = set(copy.deepcopy(t))
            j = i
            while j < len(s) and new_t:
                if s[j] in new_t:
                    new_t.remove(s[j])
                j += 1
            # print(new_t, j, i)
            if not new_t and j - i < ans[0]:
                ans = (j - i, s[i:j])
        return ans[1] if ans != (len(s), s) else ""