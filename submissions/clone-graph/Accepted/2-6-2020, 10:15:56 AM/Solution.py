// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
visited = {}
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            if not node:
                return node
            if node in visited:
                return visited[node]
            root = Node(node.val)
            visited[node] = root
            for n in node.neighbors:
                root.neighbors.append(dfs(n))
            return root
        return dfs(node)           
        