// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp_l = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                dp_l[i] = max(dp_l[i], dp_l[i-1] + 1)
                
        dp_r = [1 for _ in range(n)]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp_r[i] = max(dp_r[i], dp_r[i+1] + 1)

        ans = [0 for _ in range(n)]
        for i in range(n):
            ans[i] = max(dp_l[i], dp_r[i])
        print(ans)
        return sum(ans)