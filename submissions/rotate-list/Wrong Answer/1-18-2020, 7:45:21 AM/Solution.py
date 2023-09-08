// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        length, tail, curr = 1, head, head
        while tail.next:
            length += 1
            tail = tail.next
        k %= length
          
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head