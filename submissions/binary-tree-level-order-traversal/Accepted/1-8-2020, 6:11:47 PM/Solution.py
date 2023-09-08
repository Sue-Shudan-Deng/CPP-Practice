// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion:
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(node: TreeNode, level: int):
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                helper(node.left, level+1)
                helper(node.right, level+1)
        helper(root, 0)
        return res

# Interative:
# from collections import deque
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         else:
#             curr = root
#             res = [[]]
#             queue = [root]
#             while queue:
#                 curr = queue.pop(0)
#                 res.append(curr.val)
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#             return res
            