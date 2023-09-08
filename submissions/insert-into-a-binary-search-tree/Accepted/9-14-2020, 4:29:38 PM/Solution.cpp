// https://leetcode.com/problems/insert-into-a-binary-search-tree

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
    
// iteration:
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            return new TreeNode(val);
        }
        TreeNode* oldroot(root);
        TreeNode* hot;
        while (root && root->val != val) {
            hot = root;
            root = (val < root->val ? root->left : root->right);
        }
        if (val < hot->val) {
            hot->left = new TreeNode(val);
        } else {
            hot->right = new TreeNode(val);
        }
        return oldroot;
    }
};

// recurison:
// public TreeNode insertIntoBST(TreeNode root, int val) {
//     if (root == null) {
//         return new TreeNode(val);   // return a new node if root is null
//     }
//     if (root.val < val) {           // insert to the right subtree if val > root->val
//         root.right = insertIntoBST(root.right, val);
//     } else {                        // insert to the left subtree if val <= root->val
//         root.left = insertIntoBST(root.left, val);
//     }
//     return root;
// }