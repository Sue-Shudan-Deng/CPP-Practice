// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = list()
        l = list(set(s))
        for i in l:
            p = [x for x in range(len(s)) if s[x] == i]
            if len(p) > 1:
                q = list(map(lambda x: x[1]-x[0], zip(p[:-1], p[1:])))
                idx = q.index(max(q))
                d.append((p[idx], p[idx+1], max(q)))
        if d == list():
            return 0
        else:
            len_max = max(list(map(lambda x: x[2], d)))
            r = list(filter(lambda x: x[2] == len_max, d))[0]
            return r[1] - r[0]
    
            
                
                