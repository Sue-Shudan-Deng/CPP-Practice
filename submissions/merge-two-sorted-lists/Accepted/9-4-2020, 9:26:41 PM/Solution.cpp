// https://leetcode.com/problems/merge-two-sorted-lists

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

// //recursion
// class Solution {
// public:
//     ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
//         if (!l1 || !l2) return l1 ? l1 : l2;
//         if (l1->val < l2->val) {
//             l1->next = mergeTwoLists(l1->next, l2); 
//             return l1;
//         } else {
//             l2->next = mergeTwoLists(l1, l2->next); 
//             return l2;
//         }
//     }
// };

//iteration
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* sentinel = new ListNode(-1);
        ListNode* cur = sentinel;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                cur->next = new ListNode(l1->val);
                l1 = l1->next;
                cur = cur->next;
            } else {
                cur->next = new ListNode(l2->val);
                l2 = l2->next; 
                cur = cur->next;
            }
        }
        if (l1) cur->next = l1;
        if (l2) cur->next = l2;
        return sentinel->next;
    }
};