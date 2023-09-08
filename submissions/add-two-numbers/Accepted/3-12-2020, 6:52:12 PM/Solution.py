// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel, carry, summ = ListNode(0), 0, 0
        curr = sentinel
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summ = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            curr.next = ListNode(summ)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return sentinel.next