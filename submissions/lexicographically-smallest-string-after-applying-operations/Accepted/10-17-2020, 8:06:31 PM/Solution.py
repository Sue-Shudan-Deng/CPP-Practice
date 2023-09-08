// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dp, ans, queue = set(), s, collections.deque()
        queue.append(s)
        while queue:
            cur = queue.popleft()
            if cur in dp:
                continue
            if int(cur) < int(ans):
                ans = cur
            dp.add(cur)
            # rotate
            queue.append(cur[b:] + cur[:b])
            # add
            new_cur = ""
            for k, v in enumerate(cur):
                if k % 2:
                    new_cur += str((int(v) + a) % 10)
                else:
                    new_cur += v
            queue.append(new_cur)
        return ans