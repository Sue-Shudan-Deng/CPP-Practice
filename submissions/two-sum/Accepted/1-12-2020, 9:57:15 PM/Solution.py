// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnums = dict()
        for k, i in enumerate(nums):
            hashnums[i] = k  # 相同的数保留最后一个索引
            
        for k, n in enumerate(nums):
            left = target - n
            if hashnums.get(left) and k != hashnums[left]:
                return [k, hashnums[left]]
        return []
            