// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        else:
            rootnode = [root.val]
            leftpart = self.inorderTraversal(root.left)
            rightpart = self.inorderTraversal(root.right)
            return leftpart + rootnode + rightpart
        