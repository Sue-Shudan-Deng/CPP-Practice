// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Node:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    def __lt__(self, other):
        return self.val < other.val

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Node(l.val, l))
        while not q.empty():
            node = q.get()
            node = node.node
            point.next = ListNode(node.val)
            point = point.next
            node = node.next
            if node:
                q.put(Node(node.val, node))
        return head.next