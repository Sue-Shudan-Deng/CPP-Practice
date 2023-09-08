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
    int count = 0;
    bool countUnivalSubtreesBool(TreeNode* root) {
        if (!root) {
            return false;
        }
        if (!root->left && !root->right) {
            ++count;
            return true;
        }
        bool flag = true;
        if (root->left) {
            bool tmp = countUnivalSubtreesBool(root->left);
            if (tmp) {
                flag = flag && root->left->val == root->val;
            }
        }
        if (root->right) {
            bool tmp = countUnivalSubtreesBool(root->right);
            if (tmp) {
                flag = flag && root->right->val == root->val;
            }
        }
        if (flag) {
            ++count;
        }
        return flag;
    }
    
public:
    int countUnivalSubtrees(TreeNode* root) {
        bool res = countUnivalSubtreesBool(root);
        return count;
    }
};