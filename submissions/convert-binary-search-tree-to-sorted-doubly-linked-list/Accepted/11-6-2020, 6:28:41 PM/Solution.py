// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Inorder
        """
        if not root:
            return root
        
        def dfs(node: 'Node'):
            nonlocal first, prev
            if node:
                dfs(node.left)
                if prev:
                    node.left = prev
                    prev.right = node
                else:
                    # 最开始，把first赋值为最左边值
                    first = node
                prev = node
                dfs(node.right)
            
        first, prev = None, None
        dfs(root)
        first.left = prev # currently prev == last node in tree
        prev.right = first
        return first