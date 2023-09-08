// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for n in nums:
            if n in numset:
                return True
            else:
                numset.add(n)
        return False