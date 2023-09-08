// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = collections.defaultdict()
        s, n = s.split(), len(pattern)
        if len(pattern) != len(s):
            return False
        for i in range(n):
            c = pattern[i]
            # c in map
            if c in h:
                if s[i] != h[c]:
                    return False
            # c not in map
            else:
                if s[i] in h.values():
                    return False
                h[c] = s[i]
                
        return True
                
                