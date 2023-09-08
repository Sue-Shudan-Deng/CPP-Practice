// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         elif root.left is None and root.right is None:
#             return [root.val]
#         else:
#             rootnode = [root.val]
#             leftpart = self.inorderTraversal(root.left)
#             rightpart = self.inorderTraversal(root.right)
#             return leftpart + rootnode + rightpart

# https://www.cnblogs.com/bjwu/p/9284534.html
# 感觉是给根结点添加了两个为None的左右子结点
# 当左子树的所有结点访问完之后，保存根结点，并且访问右结点
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res