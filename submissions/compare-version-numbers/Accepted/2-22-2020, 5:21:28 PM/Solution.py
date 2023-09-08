// https://leetcode.com/problems/compare-version-numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')
        for i in range(max(len(l1), len(l2))):
            l1_val = int(l1[i]) if i < len(l1) else 0
            l2_val = int(l2[i]) if i < len(l2) else 0
            if l1_val != l2_val:
                return 1 if l1_val > l2_val else -1
        return 0