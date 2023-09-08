// https://leetcode.com/problems/flood-fill

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        这道题有点坑，需要想清楚！！！！！！！！！！！！！！！
        """
        row, col, color = len(image), len(image[0]), image[sr][sc]
        # 这一步非常重要！！！！！
        if color == newColor:
            return image
        
        def neighbors(r, c):
            for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if 0 <= nr < row and 0 <= nc < col and image[nr][nc]:
                    yield (nr, nc)
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                for nr, nc in neighbors(r, c):
                    dfs(nr, nc)
        
        dfs(sr, sc)
        return image