// https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        avg = sum(nums) / 4
        def dfs(nums: List[int], ans: List[int], idx: int, ready: int) -> bool:
            if ready == 3:
                return True
            flag = 0
            for i in range(4):
                # set
                if ans[i] + nums[idx] > avg:
                    continue
                ans[i] += nums[idx]
                if ans[i] == avg:
                    flag = 1
                # backtrack
                if dfs(nums, ans, idx+1, ready+flag):
                    return True
                # clear
                flag = 0
                ans[i] -= nums[idx]
            return False
        
        ans = [0 for _ in range(4)]
        if (sum(nums) // 4) * 4 != sum(nums):
            return False
        return dfs(nums, ans, 0, 0)

