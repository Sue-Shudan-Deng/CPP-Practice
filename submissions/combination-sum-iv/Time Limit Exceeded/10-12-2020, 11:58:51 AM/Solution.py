// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        My method: Unbounded knapsack + intentionally added combination duplicates, TLE
        """
        if not nums or min(nums) > target:
            return 0
        nums.sort()
        prev_num, flag1, flag2 = [], 0, 0
        dp = [[] for _ in range(target + 1)]
        for num in nums:
            if flag1:
                for n in prev_num:
                    if num % n == 0:
                        flag2 = 1
                        break
            if flag2:
                continue
            for i in range(num, target + 1):
                if i == num:
                    dp[num].append(collections.Counter([num]))
                else:
                    for c in dp[i - num]:
                        p = copy.deepcopy(c)
                        p[num] += 1
                        dp[i].append(p)
            flag = 1
            prev_num.append(num)
        res = dp[target]
        def perturbation(x: dict) -> int:
            p = math.factorial(sum(x.values()))
            for i in x.values():
                p /= math.factorial(i)
            return p
        return int(sum([perturbation(i) for i in res])) 