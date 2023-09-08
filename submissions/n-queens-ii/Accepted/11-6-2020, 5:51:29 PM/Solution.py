// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = [0] * n
        diag1, diag2 = [0] * (2*n-1), [0] * (2*n-1)
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        def isavaliable(r, c):
            return not col[c] and not diag1[r+c] and not diag2[r-c+n-1]
        
        def updateBoard(r, c, flag):
            col[c] = flag
            diag1[r+c] = flag
            diag2[r-c+n-1] = flag
            board[r][c] = 'Q' if flag else '.'
        
        cnt = 0
        def bt(r):
            nonlocal cnt
            if r == n:
                cnt += 1
                return
            for c in range(n):
                if isavaliable(r, c):
                    updateBoard(r, c, True)
                    bt(r+1)
                    updateBoard(r, c, False)
        bt(0)
        return cnt