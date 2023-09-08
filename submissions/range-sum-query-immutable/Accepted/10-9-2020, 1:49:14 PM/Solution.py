// https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            self.prefix = []
        else:
            self.prefix = [0 for _ in range(len(nums) + 1)]
            self.prefix[1] = nums[0]
            for i in range(2, len(nums) + 1):
                self.prefix[i] = self.prefix[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if len(self.prefix) == 0:
            return 0
        return self.prefix[j + 1] - self.prefix[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)