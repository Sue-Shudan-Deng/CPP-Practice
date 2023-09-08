// https://leetcode.com/problems/maximal-rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        build histgram + max rectangle in histgram (84)
        """
        def build_hist(row):
            res = []
            for c in range(col):
                if row == 0:
                    res.append(int(matrix[0][c] == "1"))
                else:
                    if matrix[row][c] == "0":
                        res.append(0)
                    else:
                        res.append(grid[row - 1][c] + 1)
            return res
        
        def maxrect(grid):
            stack, res = [-1], 0
            for c in range(col):
                while stack[-1] != -1 and grid[stack[-1]] >= grid[c]:
                    h = grid[stack.pop()]
                    area = h * (c - stack[-1] - 1)
                    res = max(res, area)
                stack.append(c)
                
            while stack[-1] != -1:
                h = grid[stack.pop()]
                area = h * (col - stack[-1] - 1)
                res = max(res, area)
            return res
        
        if not matrix or len(matrix) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        ans = 0
        grid = []
        for r in range(row):
            grid.append(build_hist(r))
            ans = max(ans, maxrect(grid[r]))
        return ans