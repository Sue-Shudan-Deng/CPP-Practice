// https://leetcode.com/problems/same-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<pair<TreeNode*, TreeNode*>> s;
        s.emplace(p, q);
        
        while(!s.empty()) {
            auto [p, q] = s.top();
            s.pop();            
            if (!p && !q) continue;
            if (!p || !q) return false;
            if (p->val != q->val) return false;
            s.emplace(p->right, q->right);
            s.emplace(p->left, q->left);
        }
        return true;
    }
};