// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        last_column = [matrix[i][-1] for i in range(row)]
        r = bisect.bisect_right(last_column, target)
        if r >= row:
            return False
        
        search_range = matrix[r]
        p = bisect.bisect_right(search_range, target)
        if p >= col:
            return False
        
        return matrix[r][p-1] == target