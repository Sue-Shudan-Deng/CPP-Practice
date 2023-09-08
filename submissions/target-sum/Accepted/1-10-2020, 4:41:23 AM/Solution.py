// https://leetcode.com/problems/target-sum

# 方法一：参见视频讲解，重点是理解杨辉三角以及如何用来迭代
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
    
# 方法二：转换成0 / 1 背包问题
# https://www.youtube.com/watch?v=zks6mN06xdQ 重点还是理解21min的图
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        n = len(nums)
        summ = sum(nums)
        if summ < S or (summ + S) % 2:   # 必须被2整除
            return 0
        
        target = (summ + S) // 2
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        
        for num in nums:
            tmp = copy.deepcopy(dp)
            for j in range(0, target + 1 - num):
                tmp[j + num] += dp[j]
            dp = tmp
                
        return dp[target]
                
        
        