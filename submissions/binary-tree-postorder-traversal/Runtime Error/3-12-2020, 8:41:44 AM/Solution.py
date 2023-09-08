// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        stack, res = [root], []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stacka.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]