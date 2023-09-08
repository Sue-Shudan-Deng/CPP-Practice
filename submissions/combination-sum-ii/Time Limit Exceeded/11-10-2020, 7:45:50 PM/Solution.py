// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        method 1: naive
        """
        dp = [[] for _ in range(target + 1)]
        for can in candidates:
            for i in range(target, can - 1, -1):
                if i == can:
                    dp[i].append([i])
                else:
                    for comb in dp[i - can]:
                        dp[i].append(comb + [can])
                        
        """
        https://www.geeksforgeeks.org/python-remove-all-duplicates-and-permutations-in-nested-list/ : Python | Remove all duplicates and permutations in nested list
        """
        return list(map(list, set(tuple(sorted(i)) for i in dp[target])))