// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        while head.next:
            rest = head.next.next
            new_head = head.next
            head.next = rest
            new_head.next = sentinel.next
            sentinel.next = new_head
        return sentinel.next