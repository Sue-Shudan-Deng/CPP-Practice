// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = collections.Counter(p)
        s_counter = collections.Counter()
        np, ns = len(p), len(s)
        if ns < np:
            return []
        
        ans = []
        for i in range(ns):
            s_counter[s[i]] += 1
            if i >= np:
                if s_counter[s[i-np]] == 1:
                    del s_counter[s[i-np]]
                else:
                    s_counter[s[i-np]] -= 1
            if p_counter == s_counter:
                ans.append(i-np+1)
        return ans