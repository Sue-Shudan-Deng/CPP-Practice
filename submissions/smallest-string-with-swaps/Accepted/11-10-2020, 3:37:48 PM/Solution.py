// https://leetcode.com/problems/smallest-string-with-swaps

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        method 1: BFS, TLE
        """
        # pairs = [[i[1], i[0]] if i[0] > i[1] else i for i in pairs]
        # pairs = list(set(map(tuple, pairs)))
        # queue = collections.deque([s])
        # ans = s
        # visited = set()
        # while queue:
        #     cur = queue.popleft()
        #     if cur in visited:
        #         continue
        #     visited.add(cur)
        #     ans = min(ans, cur) 
        #     for i, j in pairs:
        #         queue.append(cur[:i] + cur[j] + cur[i+1:j] + cur[i] + cur[j+1:])
        # return ans
        
        """
        method 2: Union Find
        """
        n = len(s)
        parent = [i for i in range(n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def Union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            parent[px] = py
            
        for u, v in pairs:
            Union(u, v)
            
        clique = collections.defaultdict(list)
        for i in range(n):
            clique[find(i)].append(s[i])
        
        for k in clique:
            clique[k].sort()
        res = ""
        for i in range(n):
            res += clique[find(i)].pop(0)
        return res
        
            
        

            
            
            