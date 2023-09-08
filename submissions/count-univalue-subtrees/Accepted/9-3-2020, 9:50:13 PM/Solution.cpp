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
    bool isUnival(TreeNode* root) {
        if (!root) return false;
        else if (!root->left && !root->right) {
            count ++;
            return true;
        } else {
            bool flag = true;
            if (root->left) flag &= (isUnival(root->left) && (root->left->val == root->val));
            if (root->right) flag &= (isUnival(root->right) && (root->right->val == root->val));
            if (flag) {
                count ++;
                return true;
            } else {
                return false;
            }
        }        
    } 
    
public:
    int countUnivalSubtrees(TreeNode* root) {
        bool dummy = isUnival(root);
        return count;
    }
};