// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        pre, curr = sentinel, head
        while curr:
            if curr.val == val:
                pre.next = curr.next
            pre = curr
            curr = curr.next
        return sentinel.next