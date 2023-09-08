// https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        flag, ans, j = 2, 0, 0
        s = []
        for i in range(len(tree)-1):
            if not tree[i] in s:
                if len(s) <= 2:
                    s.append(tree[i])
                if len(s) > 2:
                    ans = max(ans, i-j)
                    j = i-1
                    while tree[j] == tree[i-1]:
                        j -= 1
                    j += 1
                    s.pop(0)
        ans = max(ans, len(tree)-j)
        return ans