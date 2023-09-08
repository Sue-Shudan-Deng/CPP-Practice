// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Unbounded knapsack + intentionally added combination duplicates
        """
        if not nums or min(nums) > target:
            return 0
        dp = [[] for _ in range(target + 1)]
        for num in nums:
            for i in range(num, target + 1):
                if i == num:
                    dp[num].append([num])
                else:
                    for c in dp[i - num]:
                        dp[i].append(c + [num])
        res = [collections.Counter(i) for i in dp[target]]
        def perturbation(x: dict) -> int:
            p = math.factorial(sum(x.values()))
            for i in x.values():
                p /= math.factorial(i)
            return p
        return int(sum([perturbation(i) for i in res]))
            