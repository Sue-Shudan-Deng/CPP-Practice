// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        
        def dfs(start):
            if arr[start] == 0:
                return True
            tmp = False
            # add
            if start + arr[start] < n and not start + arr[start] in visited:
                visited.add(start + arr[start])
                tmp = tmp or dfs(start + arr[start])
            # minus
            if start - arr[start] >= 0 and not start - arr[start] in visited:
                visited.add(start - arr[start])
                tmp = tmp or dfs(start - arr[start])
            return tmp
        
        return dfs(start)