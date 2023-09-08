// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums)
        # [3,1,3,4,2]
        while l < r:
            m = l + (r - l) // 2
            cnt = 0
            for i in nums:
                if i <= m:
                    cnt += 1
            # 注：其实跟TemplateII里面的find bad version的做法是一样的  
            # 比如[1,2,3,3,3,4,5,6] => True, True, False, False,....,False
            if m < cnt:
                # (i.e. cnt >= m + 1):
                r = m
            else:
                l = m + 1
        return l