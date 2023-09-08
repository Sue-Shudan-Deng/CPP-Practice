// https://leetcode.com/problems/univalued-binary-tree

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
    bool isUnivalTree(TreeNode* root) {
        if (!root) {
            return false;
        }
        if (!root->left && !root->right) {
            return true;
        }
        bool l = isUnivalTree(root->left);
        bool r = isUnivalTree(root->right);
        if (!root->left) {
            return r && root->right->val == root->val;
        } else if (!root->right) {
            return l && root->left->val == root->val;
        } else {
            return l && r && root->left->val == root->val && root->right->val == root->val;
        }
    }
};