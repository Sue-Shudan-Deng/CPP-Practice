// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            rootnode = [root.val]
            leftnode = self.preorderTraversal(root.left)
            rightnode = self.preorderTraversal(root.right)
            return rootnode + leftnode + rightnode

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         else:
#             stack = [root]
#             res = []
#             while stack:
#                 curr = stack.pop()
#                 res.append(curr.val)
#                 // 注意：对所有孩子结点均逆序入栈
#                 if curr.right:
#                     stack.append(curr.right)
#                 if curr.left:
#                     stack.append(curr.left)
#         return res