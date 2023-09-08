// https://leetcode.com/problems/delete-node-in-a-bst

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
private:
    pair<TreeNode*, TreeNode*> successor(TreeNode* cur) {
        TreeNode* pre = cur;
        cur = cur->right;
        while (cur && cur->left) {
            pre = cur;
            cur = cur->left;
        }
        return pair<TreeNode*, TreeNode*>{pre, cur};
    }
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* oldroot(root);
        stack<TreeNode*> s;
        bool found = false;
        while (root || !s.empty()) {
            while (root) {
                s.push(root);
                root = root->left;
            }
            root = s.top();
            s.pop();
            if (root->val == key) {
                found = true;
                break;
            }
            root = root->right;
        }
        if (found) {
            if (root->left && root->right) {
                auto [hot, nxt] = successor(root);
                swap(nxt->val, root->val);
                hot->left == nxt ? hot->left = nullptr : hot->right = nullptr;
            } else {
                if (root->left) {
                    root->val = root->left->val;
                    root->left = nullptr;
                } else {
                    root->val = root->right->val;
                    root->right = nullptr;
                }
            }
        }
        return oldroot;
    }
};