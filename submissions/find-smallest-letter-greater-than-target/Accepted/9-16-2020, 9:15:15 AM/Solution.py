// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) # 注意这里一定不要减一，因为template 2的右边界是不包含的
        while l < r:
            # 按这种方式搜target(尽管target不存在),即target >= letters[m]右移
            # 但最后一定会落在恰好比target大1的位置处
            m = l + (r - l) // 2
            if target < letters[m]:
                r = m
            else:
                l = m + 1
        return letters[l % len(letters)]