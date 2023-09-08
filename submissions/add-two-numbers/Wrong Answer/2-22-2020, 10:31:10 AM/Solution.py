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
        while l1 or l2:
            p = l1.val if l1 else 0
            q = l2.val if l2 else 0
            summ = (p + q + carry) % 10
            carry = (p + q) // 10
            head.next = ListNode(summ)
            head = head.next
            print(carry, summ)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            head.next = ListNode(carry)
        return res.next