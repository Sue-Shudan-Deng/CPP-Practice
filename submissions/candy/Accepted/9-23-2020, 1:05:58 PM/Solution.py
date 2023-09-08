// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # 只为了满足左边的要求的话，这里的值应该是多少
        dp_l = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                dp_l[i] = max(dp_l[i], dp_l[i-1] + 1)
                
        # 只为了满足右边的要求的话，这里的值应该是多少
        dp_r = [1 for _ in range(n)]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp_r[i] = max(dp_r[i], dp_r[i+1] + 1)

        ans = [0 for _ in range(n)]
        for i in range(n):
            ans[i] = max(dp_l[i], dp_r[i])
        return sum(ans)