// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry, sentinel = 0, ListNode(-1)
        res = sentinel
        
        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            carry, summ = (x1 + x2 + carry) // 10, (x1 + x2 + carry) % 10
            res.next = ListNode(summ)
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        res.next = ListNode(carry) if carry else None
        return sentinel.next