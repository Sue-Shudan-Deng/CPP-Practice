// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        首先是最显然的做法: 把整个矩阵看作势能场，那么就从山腰处开始搜索
        之所以从山腰是因为两个方向分别是上下，不像山顶或山底一定是下/上
        答案选用的是左下，那么这里选择右上的点实现
        """
        if not matrix:
            return False 
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
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        分治法
        """
        if not matrix:
            return False
        def search_rec(left, up, right, down):
            if left > right or up > down:
                return False
            
            print(left, up, right, down)
            
            if matrix[up][left] > target or matrix[down][right] < target:
                return False
            
            mid = left + (right-left) // 2
            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)
        
        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)