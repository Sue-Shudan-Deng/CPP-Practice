// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        """
        难点应该在于理解题意，这里的是邻接矩阵并不是graph
        """
        n = len(M) # number of students
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        for i in range(n):
            for j in range(i, n):
                # do union op
                if M[i][j] == 1:
                    pu, pv = find(i), find(j)
                    if pu == pv:
                        continue
                    if size[pu] > size[pv]:
                        pu, pv = pv, pu
                    parent[pu] = pv
                    size[pv] += size[pu]

        # 最后必须得做下path compression
        for i in range(n):
            parent[i] = find(i)
        return len(collections.Counter(parent))
        