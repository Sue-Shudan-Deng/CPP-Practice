// https://leetcode.com/problems/word-search

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        
        def bt(r, c, suffix):
            if suffix == "":
                return True
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != suffix[0]:
                return False
            
            board[r][c] = "#"
            for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if bt(nr, nc, suffix[1:]):
                    return True
            baord[r][c] = suffix[0]
            return False
        
        for r in range(row):
            for c in range(col):
                if bt(r, c, word):
                    return True
        return False