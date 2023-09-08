// https://leetcode.com/problems/implement-trie-prefix-tree

class Trie {
    
private:
    struct TrieNode {
        TrieNode() : is_word(false), children(26, nullptr) {}
        ~TrieNode() {
            for (auto child : children) {
                if (child) {
                    delete child;
                }
            }
        }
        bool is_word;
        vector<TrieNode*> children;
    };
    
    TrieNode* find(string& prefix) {
        TrieNode* p = root.get();
        for (char c : prefix) {
            p = p->children[c - 'a'];
            if (!p) {
                break;
            }
        }
        return p;
    }
    
    std::unique_ptr<TrieNode> root;
    
public:
    /** Initialize your data structure here. */
    Trie() : root(new TrieNode()) {}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* p = root.get();
        for (char c : word) {
            if (!p->children[c - 'a']) {
                p->children[c - 'a'] = new TrieNode();
            }
            p = p->children[c - 'a'];
        }
        p->is_word = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* p = find(word);
        return p && p->is_word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return find(prefix);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */