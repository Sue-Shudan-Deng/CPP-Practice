// https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def dfs(idx, groupid, cursum, visited):
            if groupid == k:
                return True
            if cursum == avg:
                return dfs(0, groupid + 1, 0, visited)
            if cursum > avg:
                return False
            for i in range(idx, n):
                if visited[i]:
                    continue
                visited[i] = True
                if dfs(i, groupid, cursum + nums[i], visited):
                    return True
                visited[i] = False
            return False
        
        if not nums:
            return False
        nums = sorted(nums)
        summ = sum(nums)
        avg = summ // k
        if summ != avg * k:
            return False
        visited = [False for _ in range(len(nums))]
        return dfs(0, 1, 0, visited)