// https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        flag, ans, j = 2, 0, 0
        for i in range(len(tree)-1):
            if tree[i] != tree[i+1]:
                flag -= 1
                ans = max(ans, i+1-j)
            if flag == 0:
                j = i
                while tree[j] == tree[i]:
                    j -= 1
                flag += 1
        ans = max(ans, len(tree)-j)
        return ans