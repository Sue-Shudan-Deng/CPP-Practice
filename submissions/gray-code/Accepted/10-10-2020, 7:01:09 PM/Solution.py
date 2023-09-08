// https://leetcode.com/problems/gray-code

class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        https://www.youtube.com/watch?v=K3_IvifT0pI
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        dp = [0, 1]
        for i in range(2, n + 1):
            size = len(dp)
            for j in range(size - 1, -1, -1):
                dp.append(dp[j] | (1 << (i - 1)))
        return dp