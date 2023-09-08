// https://leetcode.com/problems/remove-nth-node-from-end-of-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* sentinel = new ListNode(-1);
        sentinel->next = head;
        ListNode* slow = sentinel;
        ListNode* fast = sentinel;
        
        for (int i = n; i > 0; --i) {
            fast = fast->next;
        }
        
        while (fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
        
        slow->next = slow->next->next;
        return sentinel->next;
    }
};