// https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0 for _ in range(n+1)]
        G[0], G[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1, n+1):
                G[i] += G[j-1] * G[n-j]
        
        return G[n]