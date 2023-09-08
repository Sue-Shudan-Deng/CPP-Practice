// https://leetcode.com/problems/subarrays-with-k-different-integers

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        """
        340 Longest Substring with At Most K Distinct Characters
        """
        
        def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
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
                ans += (j - i + 1)
                j += 1

            return ans
        
        return lengthOfLongestSubstringKDistinct(A, K) - lengthOfLongestSubstringKDistinct(A, K - 1)