// https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse_list_of_k(self, head: ListNode, k: int) -> (ListNode, ListNode):
        pre, cur = None, head
        for _ in range(k):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return cur, pre
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur, cnt = head, 0
        while cur and cnt < k:
            cur = cur.next
            cnt += 1
        if cnt != k:
            return head
        newhead, pre = self.reverse_list_of_k(head, k)
        head.next = self.reverseKGroup(newhead, k)
        return pre