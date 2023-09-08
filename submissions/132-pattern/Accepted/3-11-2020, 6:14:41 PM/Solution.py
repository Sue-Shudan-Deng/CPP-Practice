// https://leetcode.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        参考discussion的结果
        """
        stack = []
        s3 = float("-inf")
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and n > stack[-1]:
                s3 = stack.pop()
            stack.append(n)
        return False