// https://leetcode.com/problems/search-in-a-binary-search-tree

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

// recursion
// class Solution {
// public:
//     TreeNode* searchBST(TreeNode* root, int val) {
//         if (!root || root->val == val) return root;
//         return val < root->val ? searchBST(root->left, val) : searchBST(root->right, val);
//     }
// };

// iteration
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root || root->val == val) return root;
        while (root->val != val) root = (val < root->val ? root->left : root->right);
        return root;
    }
};