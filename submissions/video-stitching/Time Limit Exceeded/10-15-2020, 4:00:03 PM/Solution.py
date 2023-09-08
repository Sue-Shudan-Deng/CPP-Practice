// https://leetcode.com/problems/video-stitching

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x:x[0])
        clips_map = collections.defaultdict(int)
        for s, e in clips:
            clips_map[s] = max(clips_map[s], e)
        if not clips_map[0]:
            return -1
        l, r, flag, step = 0, 0, 0, 0
        while l <= r:
            new_r = 0
            for k in range(l, r + 1):
                new_r = max(new_r, clips_map[k])
            l = r
            r = new_r
            step += 1
            if new_r >= T:
                flag = 1
                break
                
        return step if flag else -1