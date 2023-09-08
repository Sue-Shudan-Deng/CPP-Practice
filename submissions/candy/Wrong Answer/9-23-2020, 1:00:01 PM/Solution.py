// https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ansl = [1 for _ in range(n)]
        for i in range(n):
            if i != n - 1 and ratings[i] > ratings[i+1]:
                ansl[i] = max(ansl[i], ansl[i+1] + 1)
            elif i != 0 and ratings[i] > ratings[i-1]:
                ansl[i] = max(ansl[i], ansl[i-1] + 1)
                
        ansr = [1 for _ in range(n)]
        for i in range(n-1, -1, -1):
            if i != n - 1 and ratings[i] > ratings[i+1]:
                ansr[i] = max(ansr[i], ansr[i+1] + 1)
            elif i != 0 and ratings[i] > ratings[i-1]:
                ansr[i] = max(ansr[i], ansr[i-1] + 1)

        ans = [1 for _ in range(n)]
        for i in range(n):
            ans[i] = max(ansl[i], ansr[i])
        return sum(ans)