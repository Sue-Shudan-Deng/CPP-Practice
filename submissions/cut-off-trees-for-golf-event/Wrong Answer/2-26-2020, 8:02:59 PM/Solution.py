// https://leetcode.com/problems/cut-off-trees-for-golf-event

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row = len(forest)
        col = len(forest[0])
        node_list = []
        for r in range(row):
            for c in range(col):
                if forest[r][c] != 0:
                    node_list.append((r, c, forest[r][c]))
        node_list = sorted(node_list, key=lambda node: node[2])
        nodes = list(map(lambda node: node[:-1], node_list))
        res = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        
        def bfs(r, c, nr, nc):
            queue = collections.deque([(r, c, 0)])
            visited = {}
            while queue:
                i, j, step = queue.popleft()
                visited[(i, j)] = True
                if i == nr and j == nc:
                    return step 
                for d in dirs:
                    new_i, new_j = i + d[0], j + d[1]
                    if new_i >= 0 and new_i <= row - 1 and new_j >= 0 and new_j <= col - 1 and forest[new_i][new_j] != 0 and not visited.get((new_i, new_j), False):
                        queue.append((new_i, new_j, step + 1))
            return float("inf")
        
        for i in range(len(nodes) - 1):
            res += bfs(nodes[i][0], nodes[i][1], nodes[i+1][0], nodes[i+1][1])
        return res if res != float("inf") else -1