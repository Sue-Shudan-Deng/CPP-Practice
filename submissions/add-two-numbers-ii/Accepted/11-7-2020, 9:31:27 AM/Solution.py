// https://leetcode.com/problems/add-two-numbers-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        head1, head2 = l1, l2
        while head1:
            s1.append(head1.val)
            head1 = head1.next
        while head2:
            s2.append(head2.val)
            head2 = head2.next
        
        head, carry = None, 0
        while s1 or s2:
            x1 = s1.pop() if s1 else 0
            x2 = s2.pop() if s2 else 0
            summ = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            node = ListNode(summ)
            node.next = head
            head = node
            
        if carry:
            node = ListNode(carry)
            node.next = head
            head = node
            
        return head