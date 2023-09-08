// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = collections.Counter(S)
        ans = 0
        for j in J:
            ans += counter[j]
        return ans