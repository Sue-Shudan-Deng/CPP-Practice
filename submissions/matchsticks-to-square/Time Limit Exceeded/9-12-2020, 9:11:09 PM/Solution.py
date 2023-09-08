// https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        avg = sum(nums) / 4
        def dfs(nums: List[int], ans: List[List[int]], idx: int) -> bool:
            if idx == len(nums):
                return sum(ans[0]) == avg and sum(ans[1]) == avg and \
                       sum(ans[2]) == avg and sum(ans[3]) == avg
            for i in range(4):
                # set
                if sum(ans[i]) + nums[idx] > avg:
                    continue
                ans[i].append(nums[idx])
                # backtrack
                if dfs(nums, ans, idx+1):
                    return True
                # clear
                ans[i].pop();
            return False
        
        ans = [[] for _ in range(4)]
        return dfs(nums, ans, 0)