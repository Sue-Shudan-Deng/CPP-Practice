// https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        flag = True
        if root.left:
            flag &= self.isUnivalTree(root.left) and root.left.val == root.val 
        if root.right:
            flag &= self.isUnivalTree(root.right) and root.right.val == root.val
        return flag