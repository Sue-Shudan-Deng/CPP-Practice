// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1 for _ in range(n)]
        for i in range(n):
            if i != n - 1 and ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1] + 1)
            elif i != 0 and ratings[i] > ratings[i-1]:
                ans[i] = max(ans[i], ans[i-1] + 1)
        return sum(ans)