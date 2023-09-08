// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]
        row = len(board)
        col = len(board[0])
        flag = False 
        pos = []
        
        def bt(r, c, prefix):
            if prefix == "":
                return True
            if r < 0 or r > row - 1 or c < 0 or c > col - 1 or board[r][c] != prefix[0]:
                return False
            # 置位, 这样以前访问过的就不能再被访问了
            board[r][c] = "#"
            for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if bt(new_r, new_c, prefix[1:]):
                    return True
            # 复位
            board[r][c] = prefix[0]
            return False
        
        for r in range(row):
            for c in range(col):
                if bt(r, c, word):
                    return True
        return False
        