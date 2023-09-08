// https://leetcode.com/problems/redundant-connection

class UnionFindSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[x] > self.rank[y]:
            self.parent[y] = px
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = py
        else:
            self.parent[y] = px
            self.rank[x] += 1 
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = UnionFindSet(len(edges))
        for x, y in edges:
            if not s.union(x, y):
                return [x, y]