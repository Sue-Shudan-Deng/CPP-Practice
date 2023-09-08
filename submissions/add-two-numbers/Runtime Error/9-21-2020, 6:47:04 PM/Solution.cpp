// https://leetcode.com/problems/add-two-numbers

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sentinel = new ListNode(-1);
        ListNode* head = sentinel;
        int p = 0, q = 0, summ = 0, carry = 0;
        
        while (l1 || l2) {
            p = l1 ? l1->val : 0;
            q = l2 ? l2->val : 0;
            summ = (p + q + carry) % 10;
            carry = (p + q + carry) / 10;
            head->next = new ListNode(summ);
            head = head->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        if (carry) {
            head->next = new ListNode(carry);
        }
        return sentinel->next;
    }
};