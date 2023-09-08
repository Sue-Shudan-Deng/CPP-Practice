// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        else:
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                ret.append(root.val)
                root = root.right
            return ret