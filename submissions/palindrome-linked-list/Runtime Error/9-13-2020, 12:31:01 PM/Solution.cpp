// https://leetcode.com/problems/palindrome-linked-list

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
    
private:
    ListNode* reverse(ListNode* head) {
        ListNode* pre(nullptr);
        ListNode* cur = head;
        ListNode* nxt;
        while (cur) {
            nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
    
    ListNode* halfpoint(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while (!fast && !fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    
public:
    bool isPalindrome(ListNode* head) {
        
        if (!head) {
            return true;
        }
        
        ListNode* half = halfpoint(head);
        ListNode* cur = reverse(half->next);
        
        while (cur) {
            if (head->val != cur->val) {
                return false;
            }
            head = head->next;
            cur = cur->next;
        }
        return true;   
    }
};