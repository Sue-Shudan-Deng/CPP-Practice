// https://leetcode.com/problems/trapping-rain-water-ii

import copy

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        up_left = copy.deepcopy(heightMap)
        up_right = copy.deepcopy(heightMap)
        bot_right = copy.deepcopy(heightMap)
        bot_left = copy.deepcopy(heightMap)

        for r in range(1, len(heightMap)):
            for c in range(1, len(heightMap[0])):
                up_left[r][c] = max(up_left[r][c], min(up_left[r-1][c],up_left[r][c-1]))
                
        for r in range(len(heightMap)-2, -1, -1):
            for c in range(1, len(heightMap[0])):                
                bot_left[r][c] = max(bot_left[r][c], min(bot_left[r+1][c],bot_left[r][c-1]))                
                
        for r in range(1, len(heightMap)):
            for c in range(len(heightMap[0])-2, -1, -1):
                up_right[r][c] = max(up_right[r][c], min(up_right[r-1][c],up_right[r][c+1]))
        
        for r in range(len(heightMap)-2, -1, -1):
            for c in range(len(heightMap[0])-2, -1, -1):
                bot_right[r][c] = max(bot_right[r][c], min(bot_right[r+1][c],bot_right[r][c+1]))

        ans = 0

        for r in range(len(heightMap)):
            for c in range(len(heightMap[0])):
                ans += min(up_left[r][c], bot_right[r][c], bot_left[r][c], up_right[r][c]) - heightMap[r][c]

        return ans