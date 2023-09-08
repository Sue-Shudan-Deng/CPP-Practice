// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        使用哨兵结点
        """
        sentinel = ListNode(0)
        sentinel.next = head
        
        curr, prev = head, sentinel
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return sentinel.next