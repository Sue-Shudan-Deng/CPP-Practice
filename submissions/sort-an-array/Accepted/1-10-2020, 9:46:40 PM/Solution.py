// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(nums), min(nums), max(nums), []
        for n in range(m, M+1):
            S.extend([n]*C[n])
        return S