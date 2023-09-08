// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, visited = len(arr), set()
        
        def dfs(start):
            if arr[start] == 0:
                return True
            tmp = False
            # add
            if start + arr[start] < n and not start + arr[start] in visited:
                visited.add(start + arr[start])
                tmp |= dfs(start + arr[start])
                visited.remove(start + arr[start])
            if tmp:
                return True
                
            # minus
            if start - arr[start] >= 0 and not start - arr[start] in visited:
                visited.add(start - arr[start])
                tmp |= dfs(start - arr[start])
                visited.remove(start - arr[start])
            return tmp
        
        return dfs(start)