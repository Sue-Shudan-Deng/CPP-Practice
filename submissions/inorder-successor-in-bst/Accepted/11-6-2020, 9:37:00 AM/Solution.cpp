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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* hot_ = nullptr;
        while (root) {
            if (root->val > p->val) {
                hot_ = root;
                root = root->left;
            } else {
                // 这里有点意思
                root = root->right;
            }
        }
        return hot_;
    }
};