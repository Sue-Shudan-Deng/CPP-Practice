// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        else:
            stack = [root]
            while stack:
                curr = stack.pop()
                ret.append(curr.val)
                if curr.left: stack.append(curr.left)
                if curr.right: stack.append(curr.right)
            return ret[::-1]