// https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # min(A[0:i]-B[0:i]) + min(B[i+1:n]-A[i+1:n])
        # = min(A[0:i]-B[0:i]) + max(A[i+1:n]-A[i+1:n])
        costs.sort(key = lambda x: x[0]-x[1])
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total