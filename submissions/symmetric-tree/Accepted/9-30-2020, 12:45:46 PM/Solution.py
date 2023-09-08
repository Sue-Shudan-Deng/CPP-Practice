// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: 
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        
        l = self.isMirror(t1.left, t2.right)
        r = self.isMirror(t2.left, t1.right)
        
        return l and r 