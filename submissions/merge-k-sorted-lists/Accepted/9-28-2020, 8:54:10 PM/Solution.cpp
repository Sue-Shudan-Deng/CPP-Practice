// https://leetcode.com/problems/merge-k-sorted-lists

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
    ListNode* merge2Lists(ListNode* list1, ListNode* list2) {
        if (!list1) {
            return list2;
        }
        if (!list2) {
            return list1;
        }
        if (list1->val < list2->val) {
            list1->next = merge2Lists(list1->next, list2);
            return list1;
        } else {
            list2->next = merge2Lists(list1, list2->next);
            return list2;
        }
    }
    
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int interval = 1, n = lists.size();
        while (interval < n) {
            for (int i = 0; i < n - interval; i += interval * 2) {
                lists[i] = merge2Lists(lists[i], lists[i + interval]); 
            }
            interval *= 2;
        }
        return lists.empty() ? nullptr : lists[0];
    }
};