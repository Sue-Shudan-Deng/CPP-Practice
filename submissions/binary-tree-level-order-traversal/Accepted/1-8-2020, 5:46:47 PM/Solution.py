// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node: TreeNode, level: int):
        if node:
            self.res[level-1].append(node.val)
            if len(self.res) == level:
                self.res.append([])
            self.helper(node.left, level+1)
            self.helper(node.right, level+1)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = [[]]
        self.helper(root, 1)
        return self.res[:-1]  # 去掉最后一个[]