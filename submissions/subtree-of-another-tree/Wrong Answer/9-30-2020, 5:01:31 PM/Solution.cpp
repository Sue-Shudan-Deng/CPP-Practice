// https://leetcode.com/problems/subtree-of-another-tree

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
    bool equal(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) {
            return true;
        }
        if (!t1 || !t2) {
            return false;
        }
        bool l = equal(t1->left, t2->left);
        bool r = equal(t1->right, t2->right);
        return l && r;
    }
    
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (!s) {
            return false;
        }
        bool l = isSubtree(s->left, t);
        bool r = isSubtree(s->right, t);
        return l || r || equal(s, t);
    }
};