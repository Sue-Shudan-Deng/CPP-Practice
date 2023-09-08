// https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def successor(root: TreeNode) -> TreeNode:
            root = root.right
            while root.left:
                root = root.left
            return root
        
        # case 1
        if not root:
            return None
        
        if root.val == key:
            # case 2
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # case 3
            succ = successor(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root