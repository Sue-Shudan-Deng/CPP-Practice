// https://leetcode.com/problems/populating-next-right-pointers-in-each-node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# # Recursive:
# # Space complexity: O(log(n))
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         """
#         用前序遍历，因为我们希望每访问一个root node就给其左右结点添加一条边
#         """
#         if not root or not root.left:
#             return root
#         # 当且仅当root及其左右结点完整时才进行操作
#         root.left.next = root.right
#         if root.next:
#             root.right.next = root.next.left
#         self.connect(root.left)
#         self.connect(root.right)
#         return root
        
# Iterative:
# Space complexity: O(1):
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        old_root = root
        # 这里是两个while循环
        while root:
            sentinel = Node(0)
            curr = sentinel
            while root:
                if root.left:
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                root = root.next
            root = sentinel.next
        return old_root
            