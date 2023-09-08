// https://leetcode.com/problems/inorder-successor-in-bst

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 下面的解法适用于任何二叉树
    // BST有更简单的做法
    // TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
    //     TreeNode* last(nullptr);
    //     stack<TreeNode*> s;
    //     while (root || !s.empty()) {
    //         while (root) {
    //             s.push(root);
    //             root = root->left;
    //         }
    //         root = s.top();
    //         s.pop();
    //         if (last == p) {
    //             return root;
    //         }
    //         last = root;
    //         root = root->right;
    //     }
    //     return nullptr;
    // }
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* hot_ = nullptr;
        while (root) {
            if (p->val < root->val) {
                hot_ = root;
                root = root->left;
            } else {
                root = root->right;
            }
        }
        return hot_;
    }
};