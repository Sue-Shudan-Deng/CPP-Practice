// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root_idx = mapping[root_val]
            root.left = helper(left_idx, root_idx - 1)
            root.right = helper(root_idx + 1, right_idx)
            return root
            
        mapping = {v:k for k, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)