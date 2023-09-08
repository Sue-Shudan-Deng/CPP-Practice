// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        340 Longest Substring with At Most K Distinct Characters
        """
        n, h = len(s), collections.defaultdict(int)
        i, j, ans = 0, 0, 0
        
        while j < n:
            h[s[j]] = j
            if len(h) == 3:
                idx = min(h.values())
                del h[s[idx]]
                i = idx + 1
                
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans