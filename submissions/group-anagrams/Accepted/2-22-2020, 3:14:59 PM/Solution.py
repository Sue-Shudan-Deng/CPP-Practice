// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 想法是把string转换成counter，如果counter match则成功
        res = dict()
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            if not res.get(tuple(counter)):
                res[tuple(counter)] = []
            res[tuple(counter)].append(s)
        return list(res.values())