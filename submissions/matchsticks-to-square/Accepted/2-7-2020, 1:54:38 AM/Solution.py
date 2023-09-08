// https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        
        def dfs(idx, groupid, tmpsum, visited):
            """
            Assume we can only search in this group 
            """
            if groupid == 4:
                return True
            if tmpsum == avg:
                # switch to the next group
                return dfs(0, groupid + 1, 0, visited)
            if tmpsum > avg:
                return False
            for i in range(idx, len(nums)):
                # If nums[i] has been visited before (same value), 
                # there is no reason to visit it twice
                if visited[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                if dfs(i + 1, groupid, tmpsum + nums[i], visited):
                    return True
                visited[i] = False
            return False
        
        if not nums:
            return False
        nums = sorted(nums)
        summ = sum(nums)
        avg = summ // 4
        if summ != avg * 4:
            return False
        visited = [False for _ in range(len(nums))]
        return dfs(0, 1, 0, visited)
            