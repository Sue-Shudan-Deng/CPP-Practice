// https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def combine(left_idx, right_idx):
            if left_idx > right_idx:
                return [None]
            
            res = []
            for idx in range(left_idx, right_idx + 1):
                left = combine(left_idx, idx - 1)
                right = combine(idx + 1, right_idx)
                for l in left:
                    for r in right:
                        root = TreeNode(idx)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        
        return combine(1, n) if n else []