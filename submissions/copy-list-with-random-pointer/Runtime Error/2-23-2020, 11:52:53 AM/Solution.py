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
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        visited = dict()
        if not head:
            return head
        if visited.get(head):
            return visited[head]
        else:
            new_node = Node(head.val)
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
            visited[head] = new_node
            return new_node