// https://leetcode.com/problems/count-univalue-subtrees

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
    int countUnivalSubtrees(TreeNode* root) {
        if (!root) {
            return 0;
        }
        if (!root->left && !root->right) {
            return 1;
        }
        int left = countUnivalSubtrees(root->left);
        int right = countUnivalSubtrees(root->right);
        bool flag;
        if (!root->right) {
            flag = root->left->val == root->val ? 1 : 0;
        }
        else if (!root->left) {
            flag = root->right->val == root->val ? 1 : 0;
        } else {
            flag = root->left->val == root->val && root->right->val == root->val ? 1 : 0;
        }
        return left + right + flag;
    }
};