// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        最基本做法(Recursion)
        1. 分别判断左右子树是否valid
        2. 分别求出左右子树的最大和最小值，和根结点比较
        """
        # Edge case
        if not root or (not root.left and not root.right):
            return True
        
        def minBST(root):
            while root.left:
                root = root.left
            return root
        
        def maxBST(root):
            while root.right:
                root = root.right
            return root
        
        left_max_valid = maxBST(root.left).val < root.val if root.left else True
        right_min_valid = root.val < minBST(root.right).val if root.right else True
        
        return self.isValidBST(root.left) and self.isValidBST(root.right) and left_max_valid and right_min_valid
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        另一种思路(Recursion)
        基本思想：确保在每一个递归部分的内部，必然满足左结点<根结点 并且 右结点>根结点 (严格)
        """
        def isvalid(root, lower=float("-inf"), upper=float("inf")):
            # Edge case
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return isvalid(root.left, lower, root.val) and isvalid(root.right, root.val, upper)
        
        return isvalid(root)
            
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Iteration
        基本思想：先序遍历，因为访问顺序是"中"左右，因此每次比较均可同时比较中间和左/右
        """
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            curr, lower, upper = stack.pop()
            if not curr:
                continue
            if curr.val <= lower or curr.val >= upper:
                return False
            stack.append((curr.right, curr.val, upper))
            stack.append((curr.left, lower, curr.val))
            
        return True
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
         """
        Iteration
        基本思想：中序遍历，必然是按照严格从小到大的顺序来访问的，这一点非常重要
        """
        stack, inorder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            # 从左结点的最左边开始
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
            
        return True
        