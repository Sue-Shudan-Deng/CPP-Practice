// https://leetcode.com/problems/maximal-network-rank

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
        rank = 0
        for i in range(n):
            for j in range(i):
                tmp = -1 if j in graph[i] else 0
                rank = max(rank, len(graph[i]) + len(graph[j]) + tmp)
        return rank