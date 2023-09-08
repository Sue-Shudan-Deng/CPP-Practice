// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        def minlen(arr: List[int], target: int) -> List[int]:
            dp = [float("inf") for _ in range(n+1)]
            prefix = [0 for _ in range(n+1)]
            for i in range(1, n+1):
                prefix[i] = prefix[i-1] + arr[i-1]
            m = {prefix[0] : 0}
            
            for i in range(1, n+1):
                dp[i] = dp[i-1]
                if target - prefix[i] in m:
                    dp[i] = min(dp[i], i - m[target-prefix[i]])
                m[prefix[i]] = i
            return dp[1:]
        
        dp_forward = minlen(arr, target)
        dp_backward = minlen(arr[::-1], target)[::-1]
        ans = float("inf")
        for i in range(0, n-1):
            ans = min(ans, dp_forward[i] + dp_backward[i+1])
        return ans