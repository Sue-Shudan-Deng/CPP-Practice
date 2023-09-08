// https://leetcode.com/problems/diagonal-traverse

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row, col = len(matrix), len(matrix[0])
        r, c = 0, 0
        upward = True
        end_r, end_c = row - 1, col - 1
        res = [matrix[r][c]]
        while True:
            while upward:
                if r == 0 and c != end_c:
                    upward = False
                    c += 1
                elif c == end_c and r != end_r:
                    upward = False
                    r += 1
                elif c == end_c and r == end_r:
                    return res
                else:
                    r, c = r - 1, c + 1
                res.append(matrix[r][c])
                    
            while not upward:
                if c == 0 and r != end_r:
                    upward = True
                    r += 1
                elif r == end_r and c != end_c:
                    upward = True
                    c += 1
                elif r == end_r and c == end_c:
                    return res
                else:
                    r, c = r + 1, c - 1
                res.append(matrix[r][c])