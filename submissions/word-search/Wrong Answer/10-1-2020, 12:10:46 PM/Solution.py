// https://leetcode.com/problems/word-search

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        row = len(board)
        col = len(board[0])
        def backtrack(r, c, rest):
            if rest == "":
                return True
            if r < 0 or r >= row or c < 0 or c >= col or rest[0] != board[r][c]:
                return False
            for new_r, new_c in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
                if backtrack(new_r, new_c, rest[1:]):
                    return True
            return False
        
        for r in range(row):
            for c in range(col):
                if backtrack(r, c, word):
                    return True
        return False
            