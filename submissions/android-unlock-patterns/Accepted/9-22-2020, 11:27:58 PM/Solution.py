// https://leetcode.com/problems/android-unlock-patterns

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        res, visited = 0, [False for _ in range(9)]
        
        def isValid(index, last_index):
            if visited[index]:
                return False
            if last_index == -1:
                return True     
            if (index + last_index) % 2 == 1:
                return True 
            mid = (index + last_index) // 2
            if mid == 4:
                return visited[mid]
            if index % 3 != last_index % 3 and index // 3 != last_index // 3:
                return True
            return visited[mid]
        
        def dfs(length, last_index):
            if length == 0:
                return 1
            summ = 0
            for i in range(9):
                if isValid(i, last_index):
                    visited[i] = True
                    summ += dfs(length - 1, i)
                    visited[i] = False
            return summ
        
        for i in range(m, n + 1):
            res += dfs(i, -1)
            visited = [False for _ in range(9)]
        return res