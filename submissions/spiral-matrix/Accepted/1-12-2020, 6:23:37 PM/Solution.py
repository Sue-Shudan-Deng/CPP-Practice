// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        all_digits = []
        for i in matrix:
            all_digits += i
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        rounds = down // 2 + 1
        res = []
        
        def go_around(res, up, down, left, right):
            row, col = up, left
            while col != right:
                res.append(matrix[row][col])
                col += 1
            if up == down:
                res.append(matrix[row][col])
                return res
            while row != down:
                res.append(matrix[row][col])
                row += 1
            if col == left:
                res.append(matrix[row][col])
                return res
            while col != left:
                res.append(matrix[row][col])
                col -= 1
            while right != left and row != up:
                res.append(matrix[row][col])
                row -= 1
            return res
            
        while set(res) != set(all_digits):
            res = go_around(res, up, down, left, right)
            if not left == right:
                left, right = left + 1, right - 1
            up, down = up + 1, down - 1
        return res
        