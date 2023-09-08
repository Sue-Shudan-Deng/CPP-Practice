// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # step 1: build undirected graph with dfs(pre-order)
        graph = collections.defaultdict(set)
        def dfs(parent, child):
            if parent and child:
                graph[parent.val].add(child.val)
                graph[child.val].add(parent.val)
            if child.left:
                dfs(child, child.left)
            if child.right:
                dfs(child, child.right)
            
        dfs(None, root)
        # step 2: bfs
        queue, res, visited = collections.deque(), [], set()
        queue.append((target.val, 0))
        while queue:
            cur, step = queue.popleft()
            if cur in visited:
                continue
            if step == K:
                res.append(cur)
                continue
            visited.add(cur)
            for nxt in graph[cur]:
                queue.append((nxt, step + 1))
    
        return res