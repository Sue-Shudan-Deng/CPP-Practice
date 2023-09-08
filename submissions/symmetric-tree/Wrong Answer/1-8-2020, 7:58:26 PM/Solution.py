// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive:
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.isMirror(root, root)
#     def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
#         if not t1 and not t2:
#             return True
#         elif not t1 or not t2:
#             return False
#         return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t2.left, t1.right)
    
# Iterative:
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque([root, root])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            print("t1:", t1)
            print("t2:", t2)
            if not t1 and not t2:
                pass
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True