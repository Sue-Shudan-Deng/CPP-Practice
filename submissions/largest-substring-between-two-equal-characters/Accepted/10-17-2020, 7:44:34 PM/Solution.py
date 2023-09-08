// https://leetcode.com/problems/largest-substring-between-two-equal-characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counter, ans = collections.defaultdict(list), -1
        for k, v in enumerate(s):
            counter[v].append(k)
        for k, v in counter.items():
            if len(v) >= 2:
                ans = max(ans, v[-1] - v[0] - 1)
        return ans