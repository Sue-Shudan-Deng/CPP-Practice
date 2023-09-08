// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        首先是最显然的做法: 把整个矩阵看作势能场，那么就从山腰处开始搜索
        之所以从山腰是因为两个方向分别是上下，不像山顶或山底一定是下/上
        答案选用的是左下，那么这里选择右上的点实现
        """
        row = len(matrix)
        col = len(matrix[0])
        r, c = 0, col - 1
        
        while r < row and c >= 0: 
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False
        
        
        
        