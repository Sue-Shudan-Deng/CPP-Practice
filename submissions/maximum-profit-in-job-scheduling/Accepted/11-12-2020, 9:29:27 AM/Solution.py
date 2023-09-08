// https://leetcode.com/problems/maximum-profit-in-job-scheduling

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
        见评论区的思路，用lee215不一样的写法实现bianry search
        """
        jobs = sorted(list(zip(startTime, endTime, profit)), key = lambda x: x[1])
        endtimes = [i[1] for i in jobs]
        n = len(jobs)
        dp = [0 for _ in range(n + 1)]
        # dp[j] maximum profit can be achieved until j
        for i, (s, e, p) in enumerate(jobs):
            pi = bisect.bisect_right(endtimes, s)
                          # 不用    #用
            dp[i+1] = max(dp[i], p + dp[pi])
            
        return dp[-1]