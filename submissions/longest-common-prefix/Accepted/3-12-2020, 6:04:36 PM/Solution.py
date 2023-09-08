// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        minlen = min(list(map(lambda x: len(x), strs)))
        """
        flag1 表示找到了，flag2 表示是否小于minlen
        """
        flag1, flag2 = False, False
        for i in range(minlen):
            if all(s[:i+1] == first[:i+1] for s in strs) and i < minlen:
                flag1, flag2 = True, True
            else:
                flag2 = False
                idx = i
                break
                
        if flag1 and not flag2:
            return first[:idx]
        elif not flag1 and not flag2:
            return ""
        else:
            return first[:minlen]
        
            
            