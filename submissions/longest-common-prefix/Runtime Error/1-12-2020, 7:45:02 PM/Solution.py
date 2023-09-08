// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        minlen = min(list(map(lambda x: len(x), strs)))
        flag1, flag2 = False, False
        for i in range(minlen):
            if all(s[:i+1] == first[:i+1] for s in strs) and i < minlen:
                flag1, flag2 = True, True
            if not all(s[:i+1] == first[:i+1] for s in strs) and i < minlen:
                flag2 = False
                idx = i
                break
                
        if flag1 and not flag2:
            return first[:idx]
        elif not flag1 and not flag2:
            return ""
        else:
            return first[:minlen]
        
            
            