// https://leetcode.com/problems/minimum-area-rectangle

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        n, ans = len(points), float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1] and (points[i][0], points[j][1]) in S and (points[j][0], points[i][1]) in S:
                    ans = min(ans, abs((points[i][0] - points[j][0]) * (points[i][1] - points[j][1])))
        return ans if ans != float("inf") else 0