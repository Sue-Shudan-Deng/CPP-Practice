// https://leetcode.com/problems/satisfiability-of-equality-equations

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        char_set = set()
        for s in equations:
            char_set.add(s[0])
            char_set.add(s[-1])
        parent = {c:c for c in char_set}
        size = {c:1 for c in char_set}
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if size[px] > size[py]:
                px, py = py, px
            parent[px] = py
            size[py] += size[px]
            return True
        
        for e in equations:
            c1, c2 = e[0], e[-1]
            op = e[1:3]
            if op == "==":
                union(c1, c2)
            else:
                if not union(c1, c2):
                    return False
        return True
            
            