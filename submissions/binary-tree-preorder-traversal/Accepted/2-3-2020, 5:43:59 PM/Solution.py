// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root == None:
#             return []
#         elif root.left == None and root.right == None:
#             return [root.val]
#         else:
#             rootnode = [root.val]
#             leftnode = self.preorderTraversal(root.left)
#             rightnode = self.preorderTraversal(root.right)
#             return rootnode + leftnode + rightnode 

# https://www.cnblogs.com/bjwu/p/9284534.html
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root == None:
#             return []
#         else:
#             stack = [root]
#             res = []
#             while stack:
#                 rootnode = stack.pop()
#                 if rootnode != None:
#                     res.append(rootnode.val)
#                     # 注意这里因为pop的出栈顺序是从右到左，
#                     # 所以右结点先进栈，可以后被访问
#                     if rootnode.right != None:
#                         stack.append(rootnode.right)
#                     if rootnode.left != None:
#                         stack.append(rootnode.left)
#             return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            stack = [root]
            res = []
            while stack:
                curr = stack.pop()
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        return res