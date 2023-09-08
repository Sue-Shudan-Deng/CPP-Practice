// https://leetcode.com/problems/redundant-connection

class UnionFindSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1 for _ in range(n+1)]
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = UnionFindSet(len(edges))
        for edge in edges:
            if not s.union(*edge):
                return edge