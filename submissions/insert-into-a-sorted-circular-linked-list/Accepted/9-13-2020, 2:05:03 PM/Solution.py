// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        def toInsert(pre: 'Node', cur: 'Node', insertVal: int) -> bool:
            # case 1
            flag1 = pre.val <= insertVal and insertVal <= cur.val
            flag2 = pre.val > cur.val and (insertVal >= pre.val or insertVal <= cur.val)
            return flag1 or flag2

        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
        
        pre, cur = head, head.next
        flag3 = False
        while True:
            if toInsert(pre, cur, insertVal):
                newNode = Node(insertVal, None)
                newNode.next = cur
                pre.next = newNode
                break
            flag3 |= pre.val == cur.val
            pre = cur
            cur = cur.next
            if pre == head:
                if flag3:
                    newNode = Node(insertVal, None)
                    newNode.next = cur
                    pre.next = newNode
                break
        return head
            
        