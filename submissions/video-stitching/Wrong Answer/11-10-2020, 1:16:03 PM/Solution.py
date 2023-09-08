// https://leetcode.com/problems/video-stitching

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        """
        method 1: Jump Game II
        """
#         clips.sort(key=lambda x:x[0])
#         clips_map = collections.defaultdict(int)
#         for s, e in clips:
#             if s != e:
#                 clips_map[s] = max(clips_map[s], e)
#         if not clips_map[0]:
#             return -1
#         l, r, flag, step = 0, 0, 0, 0
#         while l <= r:
#             new_r = 0
#             for k in range(l, r + 1):
#                 new_r = max(new_r, clips_map[k])
#             l = r
#             r = new_r
#             step += 1
#             if new_r >= T:
#                 flag = 1
#                 break
                
#         return step if flag else -1
    
        """
        method 2: 1235. Maximum Profit in Job Scheduling
        """
        clips.sort(key=lambda x:x[1])
        endtimes = [0] + [i[1] for i in clips]
        if not clips[-1][1] >= T:
            return -1
        n, res = len(clips), -1
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            s, e = clips[i-1]
            pi = bisect.bisect_left(endtimes, s)
            for j in range(i-1, pi-1, -1):
                dp[i] = min(dp[i], dp[j] + 1)
            if e >= T:
                res = max(res, dp[i])
        return res if res != float("inf") else -1