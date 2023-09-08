// https://leetcode.com/problems/delete-node-in-a-bst

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
    TreeNode* successor(TreeNode* root) {
        root = root->right;
        while (root->left) {
            root = root->left;
        }
        return root;
    }
    
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        // base case 1: root = nullptr
        if (!root) {
            return nullptr;
        }
        
        // base case 2: root->val = key, but one of the subtree is empty
        if (root->val == key) {
            if (!root->left) {
                return root->right;
            }
            if (!root->right) {
                return root->left;
            }
            
            // base case 3: none of the subtrees are empty
            TreeNode * suc = successor(root);
            root->val = suc->val;
            root->right = deleteNode(root->right, suc->val);
            return root;
        }
        
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else {
            root->right = deleteNode(root->right, key);
        }
        return root;
    }
};