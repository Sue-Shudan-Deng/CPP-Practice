// https://leetcode.com/problems/largest-sum-of-averages

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        由于这里是at most k parts, 因此神奇的可以直接用1维dp而无须K维dp
        但为了清晰还是用K维dp做,
        类似 Best time to buy and sell stocks 
        dp[k][i] = dp[k-1][j] + average(j, i)
        """
        n = len(A)
        if n == 0:
            return 0.0
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + A[i])
        
        def average(i, j):
            if j == i:
                return 0
            else:
                return (prefix_sum[j] - prefix_sum[i]) / (j - i)
            
        dp = [[0 for _ in range(n + 1)] for _ in range(K)]
        # 初始值：分成1个part，即不分
        dp[0] = [average(0, i) for i in range(n + 1)]
        
        for k in range(1, K):
            for i in range(1, n + 1):
                for j in range(1, i):
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + average(j, i))
                    
        return dp[-1][-1]