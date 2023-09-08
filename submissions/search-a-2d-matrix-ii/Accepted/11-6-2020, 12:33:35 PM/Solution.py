// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        首先是最显然的做法: 把整个矩阵看作势能场，那么就从山腰处开始搜索
        之所以从山腰是因为两个方向分别是上下，不像山顶或山底一定是下/上
        答案选用的是左下，那么这里选择右上的点实现
        比如要找25，那么搜索的路线是:15->19->22->24->30->26->23->下出界
        """
        if not matrix:
            return False 
        row, col = len(matrix), len(matrix[0])
        r, c = 0, col - 1
        
        while r < row and c >= 0: 
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False