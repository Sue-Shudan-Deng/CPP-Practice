// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l < r:
            m = l + (r - l) // 2
            if target <= letters[m]:
                r = m
            else:
                l = m + 1
        if l < 0 or l >= len(letters):
            return letters[0]
        else:
            return letters[l]