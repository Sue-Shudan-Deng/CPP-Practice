// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        row = [False for _ in range(n)]
        diag1 = [False for _ in range(2*n-1)]
        diag2 = [False for _ in range(2*n-1)]
        
        def is_not_under_attack(x, y):
            return not row[y] and not diag1[x+y] and not diag2[x-y+n-1]
        
        def update_status(x, y, isput):
            row[y] = isput
            diag1[x+y] = isput
            diag2[x-y+n-1] = isput
        
        def backtrack_nqueen(r, count):
            for c in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(r, c):
                    # explore this partial candidate solution, and mark the attacking zone
                    update_status(r, c, isput=True)
                    if r+1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(r+1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    update_status(r, c, isput=False)
            return count
        return backtrack_nqueen(0, 0)