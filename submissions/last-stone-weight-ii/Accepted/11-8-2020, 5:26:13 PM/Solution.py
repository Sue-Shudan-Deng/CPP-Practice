// https://leetcode.com/problems/last-stone-weight-ii

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        ||| a - b | - c | - d|
        联想绝对值不等式 --> 联想target sum
        或许可以剪枝，但我暂时不知道怎么搞
        """
        n, summ = len(stones), sum(stones)
        offset = summ
        dp = [[False for _ in range(summ + offset + 1)] for _ in range(n+1)]
        dp[0][offset] = True
        for i in range(1, n + 1):
            for j in range(summ + offset - stones[i-1], stones[i-1] - 1, -1):
                dp[i][j - stones[i-1]] |= dp[i-1][j]
                dp[i][j + stones[i-1]] |= dp[i-1][j]
                
        for j in range(offset, summ + offset + 1):
            if dp[n][j]:
                break
        return j - offset