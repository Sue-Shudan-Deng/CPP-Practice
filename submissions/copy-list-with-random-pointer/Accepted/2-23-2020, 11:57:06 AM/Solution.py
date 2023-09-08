// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.visited = dict()
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        if self.visited.get(head):
            return self.visited[head]
        else:
            new_node = Node(head.val)
            self.visited[head] = new_node
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
            return new_node