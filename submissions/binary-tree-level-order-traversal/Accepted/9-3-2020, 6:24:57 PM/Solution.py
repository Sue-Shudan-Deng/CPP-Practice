// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative:
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ret, level = [], 0
        queue = deque([root])
        while queue:
            ret.append([])
            level_length = len(queue)
            for i in range(level_length):
                root = queue.popleft()
                ret[level].append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            level += 1
        return ret