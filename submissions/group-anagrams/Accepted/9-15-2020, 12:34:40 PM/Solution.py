// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m  = {}
        ans = []
        idx = -1
        for s in strs:
            if m.get(tuple(sorted(s))) is None:
                m[tuple(sorted(s))] = idx + 1
                ans.append([])
                idx += 1
            ans[m[tuple(sorted(s))]].append(s)
        return ans