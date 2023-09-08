// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, level = 0):
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                if (level + 1) % 2 == 0:
                    helper(root.left, level + 1)
                    helper(root.right, level + 1)
                else:
                    helper(root.right, level + 1)
                    helper(root.left, level + 1)
            return res
        return helper(root)