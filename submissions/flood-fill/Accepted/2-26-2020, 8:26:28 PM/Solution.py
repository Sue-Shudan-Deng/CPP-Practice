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
        row = len(image)
        col = len(image[0])
        color = image[sr][sc]
        
        # 根据这道题图的性质
        if color == newColor:
            return image
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r + 1 <= row - 1: 
                    dfs(r + 1, c)
                if r - 1 >= 0:
                    dfs(r - 1, c)
                if c + 1 <= col - 1:
                    dfs(r, c + 1)
                if c - 1 >= 0:
                    dfs(r, c - 1)
        dfs(sr, sc)
        return image