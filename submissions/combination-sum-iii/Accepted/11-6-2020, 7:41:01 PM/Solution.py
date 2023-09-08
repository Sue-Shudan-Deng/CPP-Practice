// https://leetcode.com/problems/combination-sum-iii

class Solution:
    def combinationSum3(self, K: int, n: int) -> List[List[int]]:
        dp = [[] for _ in range(n + 1)]
        num_max = min(n, 9)
        for num in range(1, num_max + 1):
            for i in range(n, num-1, -1):
                if i == num:
                    dp[i].append([num])
                else:
                    for c in dp[i-num]:
                        dp[i].append(c + [num])
        return [i for i in dp[n] if len(i) == K]