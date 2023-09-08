// https://leetcode.com/problems/binary-tree-postorder-traversal

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (!root) {
            return ret;
        } else {
            stack<TreeNode*> stk;
            stk.push(root);
            while (!stk.empty()) {
                TreeNode* curr = stk.top();
                ret.push_back(curr->val);
                stk.pop();
                if (curr->left) stk.push(curr->left);
                if (curr->right) stk.push(curr->right);
            }
            reverse(ret.begin(), ret.end());
            return ret;
        }
    }
};