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
        if not root:
            return root
        
        def helper(node: 'Node'):
            nonlocal first, last
            if node:
                helper(node.left)
                if last:
                    node.left = last
                    last.right = node
                else:
                    # 最开始，把first赋值为最左边值
                    first = node
                last = node
                helper(node.right)
            
        first, last = None, None
        helper(root)
        first.left = last
        last.right = first
        return first