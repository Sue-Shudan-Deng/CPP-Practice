// https://leetcode.com/problems/filling-bookcase-shelves

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            added_w, h = 0, 0
            for j in range(i, 0, -1):
                added_w += books[j-1][0]
                if added_w > shelf_width:
                    break
                h = max(h, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + h)
        return dp[-1]