// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        rounds = down // 2 + 1
        res = []
        
        def go_around(res, up, down, left, right):
            row, col = up, left
            print(res)
            while col != right:
                res.append(matrix[row][col])
                col += 1
            print(res)
            if up == down and left == right:
                res.append(matrix[row][col])
                return res
            while row != down:
                res.append(matrix[row][col])
                row += 1
            print(res)
            while col != left:
                res.append(matrix[row][col])
                col -= 1
            print(res)
            while row != up:
                res.append(matrix[row][col])
                row -= 1
            print(res)
            return res
            
        for i in range(rounds):
            res = go_around(res, up, down, left, right)
            up, down, left, right = up + 1, down - 1, left + 1, right - 1
        return res
        