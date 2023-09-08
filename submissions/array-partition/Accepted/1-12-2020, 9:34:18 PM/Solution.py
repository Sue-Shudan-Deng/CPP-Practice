// https://leetcode.com/problems/array-partition

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        minval, maxval = -10000, 10000
        ans = 0
        counter = [0 for _ in range(2 * maxval + 1)]
        
        for n in nums:
            counter[n + maxval] += 1
            
        first = True
        for k, c in enumerate(counter):
            while c:
                if first:
                    ans += k + minval
                    first = False
                    c -= 1
                else:
                    first = True
                    c -= 1
        return ans