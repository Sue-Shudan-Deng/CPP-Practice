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

# method 1: priority queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        注：python3和python里面关于priority queue的实现不同
        并且python3里面"<"需要自行重载
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
    
# method 2: divide & conquer + merge 2 sorted list
class Solution:
    def merge2lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        in-place
        """
        if not l2:
            return l1
        if not l1:
            return l2
        if l1.val < l2.val:
            l1.next = self.merge2lists(l1.next, l2)
        else:
            l2.next = self.merge2lists(l1, l2.next)
        return l1 if l1.val < l2.val else l2
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists