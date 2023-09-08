// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        My method 1: Unbounded knapsack + intentionally added combination duplicates, TLE
        """
        # if not nums or min(nums) > target:
        #     return 0
        # nums.sort()
        # dp = [[] for _ in range(target + 1)]
        # for num in nums:
        #     for i in range(num, target + 1):
        #         if i == num:
        #             dp[num].append({num:1})
        #         else:
        #             for c in dp[i - num]:
        #                 p = copy.deepcopy(c)
        #                 p[num] = p.get(num, 0) + 1
        #                 dp[i].append(p)
        # res = dp[target]
        # def perturbation(x: dict) -> int:
        #     p = math.factorial(sum(x.values()))
        #     for i in x.values():
        #         p /= math.factorial(i)
        #     return p
        # return int(sum([perturbation(i) for i in res]))

        """
        My method 2: Reverse the for loop to satisfy the unordering property on Unbounded knapsack, passed，灵活！！！
        """
        if not nums or min(nums) > target:
            return 0
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]