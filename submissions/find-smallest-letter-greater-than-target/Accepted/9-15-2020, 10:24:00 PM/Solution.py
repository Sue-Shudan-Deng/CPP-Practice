// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) # 注意这里一定不要减一，因为template 2的右边界是不包含的
        while l < r:
            m = l + (r - l) // 2
            if target < letters[m]:
                r = m
            else:
                l = m + 1
        return letters[l % len(letters)]