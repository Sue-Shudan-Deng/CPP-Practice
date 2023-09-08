// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Iteration 版本
        """
        sentinel = ListNode(0)
        curr = sentinel
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1, curr = l1.next, curr.next
            else:
                curr.next = l2
                l2, curr = l2.next, curr.next
        curr.next = l1 if l1 else l2
        return sentinel.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Recursion 版本
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2