// https://leetcode.com/problems/array-partition

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = collections.Counter(nums)
        rest = [] # odd num of numbers
        ans = 0
        for v, n in nums.items():
            if n % 2 == 1:
                rest.append(v)
            ans += v * (n // 2)
        
        minval, maxval = min(rest), max(rest)
        first = True
        for val in range(minval, maxval + 1):
            if val in rest:
                if first:
                    ans += val
                    first = False
                else:
                    first = True
        
        return ans