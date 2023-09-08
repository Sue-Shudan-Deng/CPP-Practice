// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def __init__(self):
        self.seen = set()
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        if node in self.seen:
            return self.seen[node]
        root = Node(node.val)
        self.seen.add(root)
        for n in node.neighbors:
            root.neighbors.append(self.cloneGraph(n))
        return root            