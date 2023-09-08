// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        if not matrix or not matrix[0]:
            return 0
        
        """
        如果行数远大于列数，矩阵应该转置
        """
        
        if row > col:
            new_matrix = [[0 for _ in range(row)] for _ in range(col)]
            for r in range(row):
                for c in range(col):
                    new_matrix[c][r] = matrix[r][c]
            return self.numSubmatrixSumTarget(new_matrix, k)
        
        ans = 0
        for r1 in range(row):
            dp = [0 for _ in range(col)]
            for r2 in range(r1, row):
                # step 1 : build array
                for c in range(col):
                    dp[c] += matrix[r2][c]
                # step 2: number of subarray sum up to target, 560
                prefix = collections.defaultdict(int)
                prefix[0] = 1
                cnt, cur = 0, 0
                for num in dp:
                    cur += num
                    cnt += prefix[cur - target]
                    prefix[cur] += 1
                ans += cnt
                
        return ans