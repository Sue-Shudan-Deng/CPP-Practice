// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        如果把list整个反转过来，那么必然会用多余的空间
        因此，只反转一半的list是最好的。其次，反转之后
        的后半个list需要反转回去，原来的list不能被更改了
        """
        if not head:
            return True
        
        def reverse(node: ListNode) -> None:
            if not node or not node.next:
                return node
            sentinel = ListNode(0)
            sentinel.next = node
            while node.next:
                rest = node.next.next
                new_head = node.next
                node.next = rest
                sentinel.next = new_head
                new_head.next = node
            return sentinel.next
        
        def endhalf(node: ListNode) -> ListNode:
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Step1: 找到分割点：用2倍快慢指针
        firsthalfend = endhalf(head)
        # Step2: 反转后半部分
        reversed_secondhalf = reverse(firsthalfend.next)
        # Step3: 逐次判断
        ptr1, ptr2 = head, reversed_secondhalf
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1, ptr2 = ptr1.next, ptr2.next
        # Step4: 恢复第二部分次序
        secondhalf = reverse(reversed_secondhalf)
        firsthalfend.next = secondhalf
        return True