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
    TreeNode* hot;
    pair<TreeNode*, TreeNode*> successor(TreeNode* cur) {
        hot = cur;
        cur = cur->right;
        while (cur && cur->left) {
            hot = cur;
            cur = cur->left;
        }
        return pair<TreeNode*, TreeNode*>{hot, cur};
    }
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        hot = nullptr;
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
            hot = root;
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
                } else if (root->right) {
                    root->val = root->right->val;
                    root->right = nullptr;
                } else {
                    if (hot) {
                        hot->left = nullptr;
                        hot->right = nullptr;
                    } else {
                        return hot;
                    }
                }
            }
        }
        return oldroot;
    }
};