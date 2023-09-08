// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         """
#         Recursion:
#         这个recursion的思路真的要好好学习下，
#         上次没理解到这个精髓所在
#         """
#         if not head or not head.next:
#             return head
#         # 先到最后一个结点，再backward
#         # reversed_head永远指向最后一个结点
#         reversed_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return reversed_head
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while(curr is not None):
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        head = pre
        return head