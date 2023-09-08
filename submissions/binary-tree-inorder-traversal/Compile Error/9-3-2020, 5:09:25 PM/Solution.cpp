// https://leetcode.com/problems/binary-tree-inorder-traversal

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (root == nullptr) {
            return ret;
        } else {
            stack<TreeNode*> stk;
            stk.push(root);
            while (!stack.empty() || root != nullptr) {
                while (root != nullptr) {
                    root = root->left;
                    stk.push(root);
                }
                root = stk.top();
                ret.push_back(root->val);
                stk.pop();
                stk.push(root->right);
            }
            return ret;
        }
    }
};