// https://leetcode.com/problems/license-key-formatting

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = "".join(S.split('-')).upper()
        first = len(s) % K if len(s) % K else K
        ans = s[:first] + '-'
        for i in range(first, len(s), K):
            ans += (s[i:i+K] + '-')
        return ans[:-1]