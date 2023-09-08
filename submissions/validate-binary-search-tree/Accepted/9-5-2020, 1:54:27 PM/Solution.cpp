// https://leetcode.com/problems/validate-binary-search-tree

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

// Iteration, 中序遍历
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> stack;
        int last = INT_MIN;
        int counter = 0;
        while (root || !stack.empty()) {
            while (root) {
                stack.push(root);
                root = root->left;
            }
            root = stack.top();
            stack.pop();
            if (root->val <= last && counter != 0) return false;
            if (counter == 0) counter++;
            last = root->val;
            root = root->right;
        }
        return true;
    }
};