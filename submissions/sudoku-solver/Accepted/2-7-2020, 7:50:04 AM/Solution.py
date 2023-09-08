// https://leetcode.com/problems/sudoku-solver

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Step1: store original board by row, col and box
        
        row = [[0 for _ in range(10)] for _ in range(9)]
        col = [[0 for _ in range(10)] for _ in range(9)]
        box = [[0 for _ in range(10)] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = (j // 3) * 3 + (i // 3)
                    char = int(board[i][j])
                    row[i][char] = 1
                    col[j][char] = 1
                    box[n][char] = 1
        
        def update(i, j, char, board, isSet):
            n = (j // 3) * 3 + (i // 3)
            row[i][char] = isSet
            col[j][char] = isSet
            box[n][char] = isSet
            board[i][j] = str(char) if isSet else '.'
        
        def bt(x = 0, y = 0, board=board):
            if y == 9:
                return True
            
            nx = (x + 1) % 9
            ny = y + 1 if nx == 0 else y
            
            if board[x][y] != '.':
                return bt(nx, ny, board)
            
            for n in range(1, 10):
                if not row[x][n] and not col[y][n] and not box[(y//3)*3+(x//3)][n]:
                    update(x, y, n, board, isSet=1)
                    if bt(nx, ny):
                        return True
                    update(x, y, n, board, isSet=0)
            return False
        
        bt()