// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n, h = len(s), collections.defaultdict(int)
        if n == 0 or k == 0:
            return 0
        i, j, ans = 0, 0, 0
        
        while j < n:
            h[s[j]] = j
            if len(h) == k + 1:
                # remove the one with smallest index
                idx = min(h.values())
                del h[s[idx]]
                i = idx + 1
                ans = max(ans, j - idx)
            j += 1
            ans = max(ans, j - i)
            
        return ans