// https://leetcode.com/problems/path-sum

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
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) {
            return false;
        }
        if (!root->left && !root->right) {
            return sum == root->val;
        }
        bool l, r;
        if (root->left) {
            l = hasPathSum(root->left, sum - root->val);
        }
        if (root->right) {
            r = hasPathSum(root->right, sum - root->val);
        }
        return l || r;
    }
};