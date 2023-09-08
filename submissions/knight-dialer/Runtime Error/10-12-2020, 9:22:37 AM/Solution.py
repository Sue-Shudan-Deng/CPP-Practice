// https://leetcode.com/problems/knight-dialer

class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        # possible moves for each index i
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        
        dp = [[0 for _ in range(10)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for k, nei in enumerate(moves):
                if i == 1:
                    dp[i][k] += 1
                else:
                    dp[i][k] = (dp[i][k] + dp[i-1][nei]) % mod
                    
        return sum(dp[-1])