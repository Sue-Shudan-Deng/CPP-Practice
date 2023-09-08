// https://leetcode.com/problems/group-anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = dict()  
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            if not res.get(tuple(counter)):
                res[tuple(counter)] = []
            res[tuple(counter)].append(s)
        return list(res.values())