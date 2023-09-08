// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_counter = collections.Counter(s1)
        s2_counter = collections.Counter(s2)
        s3_counter = collections.Counter(s3)
        for k, v in s3_counter.items():
            if s1_counter.get(k, 0) + s2_counter.get(k, 0) != v:
                return False
        return True