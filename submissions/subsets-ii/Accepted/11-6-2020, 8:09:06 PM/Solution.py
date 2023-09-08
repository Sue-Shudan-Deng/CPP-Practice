// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []
        def bt(start, length, cur):
            if start == length:
                ans.append(cur[:])
                return
            for idx in range(start, n):
                bt(idx + 1, length, cur + [nums[idx]])
        
        for k in range(n + 1):
            bt(0, k, [])
        return list(set(map(tuple, [sorted(i) for i in sorted(map(tuple, ans))])))