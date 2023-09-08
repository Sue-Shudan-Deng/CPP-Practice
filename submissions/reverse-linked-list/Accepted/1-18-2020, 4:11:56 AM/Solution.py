// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Recursion:
        这个recursion的思路真的要好好学习下，
        上次没理解到这个精髓所在
        """
        if not head or not head.next:
            return head
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Iteration:
        
        """
        if not head or not head.next:
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