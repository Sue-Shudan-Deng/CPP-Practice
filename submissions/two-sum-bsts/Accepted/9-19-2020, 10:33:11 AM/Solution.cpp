// https://leetcode.com/problems/two-sum-bsts

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
    set<int> inorder(TreeNode* root, int target) {
        set<int> res;
        if (!root) {
            return res;
        }
        stack<TreeNode*> s;
        while (root || !s.empty()) {
            while (root) {
                s.push(root);
                root = root->left;
            }
            root = s.top();
            s.pop();
            res.insert(target - root->val);
            root = root->right;
        }
        return res;
    }
    
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        set<int> inorderTree1 = inorder(root1, target);
        if (inorderTree1.empty() || !root2) {
            return false;
        }
        stack<TreeNode*> s;
        while (root2 || !s.empty()) {
            while (root2) {
                s.push(root2);
                root2 = root2->left;
            }
            root2 = s.top();
            s.pop();
            if (inorderTree1.count(root2->val)) {
                return true;
            } 
            root2 = root2->right;
        }
        return false;
    }
};