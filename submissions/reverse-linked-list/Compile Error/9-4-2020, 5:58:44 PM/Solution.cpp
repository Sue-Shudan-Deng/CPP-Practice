// https://leetcode.com/problems/reverse-linked-list

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

// recursion
// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
//         if (!head || !head->next) return head;
//         ListNode* reversed_head = reverseList(head->next);
//         head->next->next = head;
//         head->next = nullptr;
//         return reversed_head;
//     }
// };

// iteration
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = nullptr, cur = head, nxt = nullptr;
        while (cur) {
            nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
};