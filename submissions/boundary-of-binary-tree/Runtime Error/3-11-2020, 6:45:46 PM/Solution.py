// https://leetcode.com/problems/boundary-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        """
        三个dfs解决
        """
        def dfs_leftmost(node: TreeNode):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)
                
        def dfs_leaves(node: TreeNode):
            if not node:
                return 
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)
            
        def dfs_rightmost(node: TreeNode):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                dfs_leftmost(node.right)
            else:
                dfs_leftmost(node.left)
            boundary.append(node.val)
            
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary