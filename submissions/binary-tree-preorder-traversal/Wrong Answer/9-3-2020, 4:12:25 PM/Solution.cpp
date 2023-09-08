// https://leetcode.com/problems/binary-tree-preorder-traversal

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
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            vector<int> ret;
            return ret;
        }
        if (root->left == nullptr && root->right == nullptr) {
            vector<int> ret{root->val};
            return ret;
        }
        
        vector<int> v1 = preorderTraversal(root->right);
        v1.push_back(root->val);
        vector<int> v2 = preorderTraversal(root->left);
        v1.insert(v1.end(), v2.begin(), v2.end());
        return v1;
    }
};