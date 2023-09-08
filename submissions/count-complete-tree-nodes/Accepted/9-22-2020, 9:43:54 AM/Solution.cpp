// https://leetcode.com/problems/count-complete-tree-nodes

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
    int computeDepth(TreeNode* root) {
        // 根据最后一层最左边的node即可判断
        // root节点位于level 0
        int d = 0;
        while (root->left) {
            ++d;
            root = root->left;
        }
        return d;
    }
    
    TreeNode* exist(int idx, int d, TreeNode* root) {
        int l = 0, r = pow(2, d) - 1, m = 0;
        for (int i = 0; i < d; ++i) {
            // 这样写，退出的时候l=r，没啥问题
            m = l + (r - l) / 2;
            if (idx <= m) {
                // 这里取 r = m 而不是 r = m - 1 并不是无缘无故的，
                // 因为上面的判断是包含了idx == m
                // 可以用这种方式来记忆
                r = m;
                root = root->left;
            } else {
                l = m + 1;
                root = root->right;
            }
        }
        return root ? root : nullptr;
    }
    
public:
    int countNodes(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int d = computeDepth(root);
        if (d == 0) {
            return 1;
        }
        int l = 0, r = pow(2, d) - 1, m = 0;
        while (l <= r) {
            // 退出条件：l = r + 1，合理，因为我们需要node的个数而不是index
            m = l + (r - l) / 2;
            if (exist(m, d, root)) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return pow(2, d) - 1 + l;
    }
};