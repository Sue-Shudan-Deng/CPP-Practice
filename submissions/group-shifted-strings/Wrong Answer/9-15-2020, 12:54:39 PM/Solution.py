// https://leetcode.com/problems/group-shifted-strings

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strings:
            k = tuple((ord(ch) - ord(s[0]) for ch in s))
            ans[k].append(s)
        return list(ans.values())