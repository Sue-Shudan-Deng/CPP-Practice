// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        old_root = root
        # intra-level
        while root:
            sentinel = Node(0)
            curr = sentinel
            # inner-level:
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