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
    
private:
    bool countUnivalSubtreesBool(TreeNode* root, int& count) {
        if (!root) {
            return false;
        }
        if (!root->left && !root->right) {
            ++count;
            return true;
        }
        bool left = countUnivalSubtreesBool(root->left, count);
        bool right = countUnivalSubtreesBool(root->right, count);
        bool flag;
        if (!root->right) {
            flag = left && root->left->val == root->val;
        } else if (!root->left) {
            flag = right && root->right->val == root->val;
        } else {
            flag = left && right && root->left->val == root->val && root->right->val == root->val;
        }
        if (flag) {
            ++count;
        }
        return flag;
    }
    
public:
    int countUnivalSubtrees(TreeNode* root) {
        int count = 0;
        bool res = countUnivalSubtreesBool(root, count);
        return count;
    }
};