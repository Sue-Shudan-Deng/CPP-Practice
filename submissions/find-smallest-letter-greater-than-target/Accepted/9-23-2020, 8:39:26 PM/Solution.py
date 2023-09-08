// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) # 这里允许数组越界
        while l < r:
            m = l + (r - l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l % len(letters)]