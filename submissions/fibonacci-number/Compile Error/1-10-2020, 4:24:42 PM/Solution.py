// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, N: int) -> int:
        """
        用双指针，避免存储O(N)
        """
        prev1 = 0 
        prev2 = 1
        curr = 0 if N = 0 else 1
        
        for i in range(N-1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
            
        return curr