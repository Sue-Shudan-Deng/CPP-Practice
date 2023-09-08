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

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            stack = [root]
            res = []
            while stack:
                rootnode = stack.pop()
                res.append(rootnode.val)
                if rootnode.left != None:
                    stack.append(rootnode.left)
                if rootnode.right != None:
                    stack.append(rootnode.right)
            return res