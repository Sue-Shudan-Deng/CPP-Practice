// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# DFS
class Solution:
    def __init__(self):
        self.visited = dict()
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        1. 找到图中所有点
        2. 复制图中所有点，一一对应
        3. 复制点对应的边
        """
        # edge case
        if not node:
            return node
        # 1.已经找到过这个点
        if self.visited.get(node):
            return self.visited[node]
        # 2.先复制结点，再复制neighbors
        else:
            new_node = Node(node.val, [])
            self.visited[node] = new_node
            if node.neighbors:
                new_node.neighbors = [self.cloneGraph(nei) for nei in node.neighbors]
        return new_node