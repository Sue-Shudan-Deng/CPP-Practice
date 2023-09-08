// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        r, c = 0, col - 1
        while r < row and c >= 0:
            if matrix[r][c] > target:
                r += 1
            elif matrix[r][c] < target:
                c -= 1
            else:
                return True
        return False