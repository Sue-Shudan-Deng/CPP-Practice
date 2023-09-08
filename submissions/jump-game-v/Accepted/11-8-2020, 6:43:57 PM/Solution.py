// https://leetcode.com/problems/jump-game-v

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """
        难点：1.sort  2.取max
        """
        arr_index, n = [], len(arr)
        for k, v in enumerate(arr):
            arr_index.append((k, v))
        arr_index.sort(key=lambda x:x[1])
        # 从小到大排序，为了 1.greedy 2.无后效性
        dp = [1 for _ in range(n)]
        
        for i, h in arr_index:
            j = i + 1
            while j <= min(n - 1, i + d) and arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                j += 1
            j = i - 1
            while j >= max(0, i - d) and arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                j -= 1
            
        return max(dp)