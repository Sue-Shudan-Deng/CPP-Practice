// https://leetcode.com/problems/maximize-distance-to-closest-person

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        f = [0 for _ in range(n)]
        b = [0 for _ in range(n)]
        
        left = float("inf")
        for i in range(n):
            if seats[i] == 1:
                left = i
            else:
                f[i] = i - left
        
        right = float("inf")
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right = i
            else:
                b[i] = right - i
            
        cur, res = float("-inf"), -1
        for i in range(n):
            if not seats[i] and min(f[i], b[i]) > cur:
                res = i
                cur = min(f[i], b[i])
        return res