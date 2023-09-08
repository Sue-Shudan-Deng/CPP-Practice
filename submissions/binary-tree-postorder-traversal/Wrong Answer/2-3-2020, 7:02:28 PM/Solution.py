// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 后序遍历是前序遍历交换左右子树之后的倒序
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         else:
#             stack = [root]
#             res = []
#             while stack:
#                 rootnode = stack.pop()
#                 res.append(rootnode.val)
#                 if rootnode.left is not None:
#                     stack.append(rootnode.left)
#                 if rootnode.right is not None:
#                     stack.append(rootnode.right)
#         return res[::-1]
    
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            stack = [root]
            res = []
            while stack:
                curr = stack.pop()
                res.append(curr)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return res[::-1]