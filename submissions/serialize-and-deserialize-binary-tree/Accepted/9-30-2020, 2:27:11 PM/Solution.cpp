// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
    
private:
    void rserialize(TreeNode* root, string& cur) {
        if (!root) {
            cur += "None,";
            return;
        }
        cur += to_string(root->val) + ",";
        rserialize(root->left, cur);
        rserialize(root->right, cur);
    }
    
    TreeNode* rdeserialize(deque<string>& cur) {
        if (cur.front() == "None") {
            cur.pop_front();
            return nullptr;
        }
        TreeNode* root = new TreeNode(stoi(cur.front()));
        cur.pop_front();
        root->left = rdeserialize(cur);
        root->right = rdeserialize(cur);
        return root;
    }
    
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string cur = "";
        rserialize(root, cur);
        return cur.substr(0, cur.size() - 1);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string s) {
        size_t pos = 0;
        deque<string> cur;
        string delim = ",";
        while (s.find(delim) != string::npos) {
            pos = s.find(delim);
            cur.push_back(s.substr(0, pos));
            s.erase(0, pos + delim.size());
        }
        cur.push_back(s);
        return rdeserialize(cur);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));