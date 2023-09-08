// https://leetcode.com/problems/word-pattern-ii

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        h = collections.defaultdict(str)
        def dfs(pattern, s):
            if len(pattern) == 0:
                return len(s) == 0
            
            c = pattern[0]
            if c in h:
                if s[:len(h[c])] != h[c]:
                    return False
                else:
                    return dfs(pattern[1:], s[len(h[c]):])
            else:
                n = len(s)
                for i in range(n):
                    word = s[:i]
                    if word in h.values():
                        continue
                    h[c] = word
                    if dfs(pattern[1:], s[len(word):]):
                        return True
                    del h[c]
                    
            return False
        
        return dfs(pattern, s)