// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        https://www.youtube.com/watch?v=RZVPX3elY9I&t=487s
        """
        row, col = len(matrix), len(matrix[0])
        if not matrix or not matrix[0]:
            return 0
        ans = float("-inf")
        for r1 in range(row):
            dp = [0 for _ in range(col)]
            for r2 in range(r1, row):
                # step 1 : build array
                for c in range(col):
                    dp[c] += matrix[r2][c]
                # step 2: max subarray no larger than K
                prefix = [0 for _ in range(col + 1)]
                prefix[1] = dp[0]
                for i in range(2, col + 1):
                    prefix[i] = prefix[i - 1] + dp[i - 1]
                
                cur = [[0, 0]]
                for j in range(1, col + 1):
                    p = bisect.bisect_left(cur, [prefix[j] - k])
                    if p < len(cur):
                        ans = max(ans, prefix[j] - prefix[cur[p][1]])
                    bisect.insort(cur, [prefix[j], j])
        return ans
        