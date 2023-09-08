// https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = [False for _ in range(n)]
        diag1 = [False for _ in range(2*n-1)]
        diag2 = [False for _ in range(2*n-1)]
        queens = set()  # 只记录queens的位置即可，没必要记录整个棋盘
        res = []
        
        def is_not_under_attack(x, y):
            return not row[y] and not diag1[x+y] and not diag2[x-y+n-1]
        
        def update_status(x, y, isput):
            row[y] = isput
            diag1[x+y] = isput
            diag2[x-y+n-1] = isput
            queens.add((x, y)) if isput else queens.remove((x, y))
        
        def add_solution():
            sol = []
            for _, c in sorted(queens):
                sol.append('.' * c + 'Q' + '.' * (n-c-1))
            res.append(sol)
        
        def backtrack_nqueen(r):
            for c in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(r, c):
                    # explore this partial candidate solution, and mark the attacking zone
                    update_status(r, c, isput=True)
                    if r+1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        add_solution()
                    else:
                        # we move on to the next row
                        backtrack_nqueen(r+1)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    update_status(r, c, isput=False)

        backtrack_nqueen(0)
        return res
        