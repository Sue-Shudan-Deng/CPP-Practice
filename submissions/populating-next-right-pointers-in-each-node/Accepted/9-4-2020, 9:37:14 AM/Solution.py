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