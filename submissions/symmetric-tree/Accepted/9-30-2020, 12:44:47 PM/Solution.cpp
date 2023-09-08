// https://leetcode.com/problems/symmetric-tree

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
    
bool isSymmetric2(TreeNode* root1, TreeNode* root2) {
    if (!root1 && !root2) {
        return true;
    }
    if (!root1 || !root2 || root1->val != root2->val) {
        return false;
    }
    bool left = isSymmetric2(root1->left, root2->right);
    bool right = isSymmetric2(root1->right, root2->left);
    return left && right;
}
    
    
public:
    bool isSymmetric(TreeNode* root) {
        return isSymmetric2(root, root);
    }
};