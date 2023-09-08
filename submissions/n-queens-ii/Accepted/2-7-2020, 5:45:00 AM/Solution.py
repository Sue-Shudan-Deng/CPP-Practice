// https://leetcode.com/problems/n-queens-ii

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = [False for _ in range(n)] 
        diag1 = [False for _ in range(2 * n - 1)]
        diag2 = [False for _ in range(2 * n - 1)]
        
        def is_under_attack(x, y):
            return col[y] or diag1[x + y] or diag2[x - y + n - 1]
        
        def update(x, y, isTrue):
            col[y] = isTrue
            diag1[x + y] = isTrue
            diag2[x - y + n - 1] = isTrue
            
        def bt(r = 0, cnt = 0):
            for c in range(n):
                if not is_under_attack(r, c):
                    update(r, c, isTrue=True)
                    if r + 1 == n:
                        cnt += 1
                    else:
                        cnt = bt(r + 1, cnt)
                    update(r, c, isTrue=False)
            return cnt
        return bt(0)