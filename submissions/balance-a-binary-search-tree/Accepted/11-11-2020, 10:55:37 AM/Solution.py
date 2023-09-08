// https://leetcode.com/problems/balance-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # step 1: build inorder sorted array
        nums = [] 
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        def build_BBST(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = build_BBST(l, m - 1)
            root.right = build_BBST(m + 1, r)
            return root
            
        inorder(root)
        return build_BBST(0, len(nums) - 1)