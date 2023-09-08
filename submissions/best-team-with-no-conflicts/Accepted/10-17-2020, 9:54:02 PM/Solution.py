// https://leetcode.com/problems/best-team-with-no-conflicts

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        这里的dp真的有点巧妙
        union-find是不成立的：比如0,2是互斥的，但0,3和2,3可能都不是互斥的
        """
        n = len(scores)
        dp, res = [0 for _ in range(n)], 0
        scores_ages = sorted(list(zip(ages, scores)))
        """
        这里的重点反而是这个sort函数，
        自带的相当于group by了再sort
        """
        for i in range(n):
            ai, si = scores_ages[i]
            dp[i] = si
            for j in range(i):
                aj, sj = scores_ages[j]
                """
                因此这里如果sj > si了必然是不行的，而无需aj < ai and sj > si
                """
                if sj > si:
                    continue
                dp[i] = max(dp[i], dp[j] + si)
            res = max(res, dp[i])
        return res