// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m  = {}
        ans = []
        idx = -1
        for s in strs:
            if m.get("".join(sorted(s))) is None:
                m["".join(sorted(s))] = idx + 1
                ans.append([])
                idx += 1
            ans[m["".join(sorted(s))]].append(s)
        return ans