// https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS: 成立条件: 左右子树分别是univaltree并且左右子树的最上方结点等于根结点
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.isunival(root)
        return self.count
        
    def isunival(self, root: TreeNode) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            self.count += 1
            return True
        flag = True
        if root.left:
            flag &= (self.isunival(root.left) and root.left.val == root.val)
        if root.right:
            flag &= (self.isunival(root.right) and root.right.val == root.val)
        if flag:
            self.count += 1
            return True
        else:
            return False