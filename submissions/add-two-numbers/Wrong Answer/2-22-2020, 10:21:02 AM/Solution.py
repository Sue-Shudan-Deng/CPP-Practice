// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        # sentinel node
        res = ListNode(0)
        head = res
        while l1 and l2:
            summ = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val) // 10
            head.next = ListNode(summ)
            head = head.next
            l1, l2 = l1.next, l2.next
        while l1:
            summ = (l1.val + carry) % 10
            carry = l1.val // 10
            head.next = ListNode(summ)
            head = head.next
            l1 = l1.next
        while l2:
            summ = (l2.val + carry) % 10
            carry = l2.val // 10
            head.next = ListNode(summ)
            head = head.next
            l2 = l2.next
        return res.next