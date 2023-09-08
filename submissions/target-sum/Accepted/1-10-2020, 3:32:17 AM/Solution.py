// https://leetcode.com/problems/target-sum

# 参见视频讲解，重点是理解杨辉三角以及如何用来迭代
# https://www.youtube.com/watch?v=r6Wz4W1TbuI&t=1239s
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        n = len(nums)
        summ = sum(nums)
        if summ < S:
            return 0
         
        # 这里的offset是必要的，为了使得二维数组的第二维index合法
        offset = summ  
        # 注意这样初始化才合法
        ways = [[0 for _ in range(summ + offset + 1)] for _ in range(n+1)]
        # 参考杨辉三角，相当于把ways[0][0] = 1
        ways[0][offset] = 1
        
        for i in range(n):
            for j in range(nums[i], summ + offset + 1 - nums[i]):
                if ways[i][j]:
                    ways[i + 1][j - nums[i]] += ways[i][j]
                    ways[i + 1][j + nums[i]] += ways[i][j]
                    
        return ways[n][S+offset]