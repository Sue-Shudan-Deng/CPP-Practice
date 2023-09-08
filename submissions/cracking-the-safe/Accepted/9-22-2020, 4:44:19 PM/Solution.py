// https://leetcode.com/problems/cracking-the-safe

class Solution(object):
    def crackSafe(self, n, k):
        seen = set()
        ans = []
        def dfs(node):
            for x in range(k):
                x = str(x)
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)