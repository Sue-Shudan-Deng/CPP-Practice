// https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        avg = sum(nums) / 4
        def dfs(nums: List[int], ans: List[int], idx: int, ready: int) -> bool:
            if idx == len(nums):
                return ready == 4
            for i in range(4):
                # set
                if ans[i] + nums[idx] > avg:
                    continue
                elif ans[i] + nums[idx] == avg:
                    ready += 1
                ans[i] += nums[idx]
                # backtrack
                if dfs(nums, ans, idx+1, ready):
                    return True
                # clear
                ans[i] -= nums[idx]
            return False
        
        ans = [0 for _ in range(4)]
        return dfs(nums, ans, 0, 0)