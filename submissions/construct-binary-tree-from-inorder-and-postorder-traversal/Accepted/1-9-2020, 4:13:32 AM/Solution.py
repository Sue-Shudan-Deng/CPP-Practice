// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion:
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left_index, right_index):
            if left_index > right_index:
                return None
            # 注：答案的解法压根没刻意分割postorder
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_index = mapping[root_val]
            # 关键是先从右边开始
            root.right = helper(root_index + 1, right_index)
            root.left = helper(left_index, root_index - 1)
            return root
            
        mapping = {v:k for k,v in enumerate(inorder)}
        return helper(0, len(postorder) - 1)