// https://leetcode.com/problems/unique-binary-search-trees-ii

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
    vector<TreeNode*> generateTrees(int left, int right) {
        if (left > right) {
            vector<TreeNode*> tmp{nullptr};
            return tmp;
        }
        vector<TreeNode*> left_trees;
        vector<TreeNode*> right_trees;
        vector<TreeNode*> ret;
        for (auto k=left; k<=right; ++k) {
            left_trees = generateTrees(left, k-1);
            right_trees = generateTrees(k+1, right);
            for (auto i : left_trees) {
                for (auto j : right_trees) {
                    TreeNode* cur = new TreeNode(k);
                    cur->left = i;
                    cur->right = j;
                    ret.push_back(cur);
                }
            }
        }
        return ret;
    }
    
public:
    vector<TreeNode*> generateTrees(int n) {
        vector<TreeNode*> tmp;
        return n ? generateTrees(1, n) : tmp;
    }
};