// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion:
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []
#         def helper(node: TreeNode, level: int):
#             if node:
#                 if len(res) == level:
#                     res.append([])
#                 res[level].append(node.val)
#                 helper(node.left, level+1)
#                 helper(node.right, level+1)
#         helper(root, 0)
#         return res

# Interative:
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
        res = []
        queue = deque([root])
        while queue:
            res.append([])
            # 原则: 对于每一层，先把改层对应的queue的总长度作为
            # queue的长度，然后清空queue
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if node:
                    res[level].append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level += 1
            
        return res
            
        
            
            