// https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_list_of_k(self, head: ListNode, k: int) -> (ListNode, ListNode):
        # 注：由于python按引用传递，这里采取最安全的做法：用迭代版本来做
        # return: head of next group, next_head
        pre, cur = None, head
        assert k > 1
        for _ in range(k):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return cur, pre
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cnt = 0
        cur = head
        while cnt < k and cur:
            cur = cur.next
            cnt += 1
        if cnt < k:
            return head
        new_head, pre = self.reverse_list_of_k(head, k)
        head.next = self.reverseKGroup(new_head, k)
        return pre