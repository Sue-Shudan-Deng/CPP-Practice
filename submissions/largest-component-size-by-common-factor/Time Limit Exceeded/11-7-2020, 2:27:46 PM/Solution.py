// https://leetcode.com/problems/largest-component-size-by-common-factor

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = {a:a for a in A}
        size = {a: 1 for a in A}
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
            
        def gcd(x, y):
            if y == 0: 
                return x 
            else: 
                return gcd(y, x % y)
            
        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                if gcd(A[i], A[j]) > 1:
                    union(A[i], A[j])
                    
        return max(size.values())