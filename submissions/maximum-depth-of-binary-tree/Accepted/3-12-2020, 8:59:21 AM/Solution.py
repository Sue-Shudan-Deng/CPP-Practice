// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Top to Down 的先序遍历
        """
        if not root:
            return 0
        stack, ans = [(root, 1)], 1
        while stack:
            root, depth = stack.pop()
            ans = max(ans, depth)
            if root.right:
                stack.append((root.right, depth + 1))
            if root.left:
                stack.append((root.left, depth + 1))
        return ans