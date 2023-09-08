// https://leetcode.com/problems/map-sum-pairs

class MapSum {
    
private:
    struct TrieNode {
        TrieNode(): children(128, nullptr) {}
        ~TrieNode() {
            for (auto child : children) {
                if (child) {
                    delete child;
                }
            }
            children.clear();
        }
        vector<TrieNode*> children;
        int sum = 0;
    };

    std::unique_ptr<TrieNode> root;
    unordered_map<string, int> vals;
    
public:
    /** Initialize your data structure here. */
    MapSum() : root(new TrieNode()) {}
    
    void insert(string key, int val) {
        int inc = val;
        if (vals.count(key)) {
            inc -= vals[key];
        }
        vals[key] = val;
        TrieNode *p = root.get(); 
        for (auto c : key) {
            if (!p->children[c]) {
                p->children[c] = new TrieNode();
            }
            p = p->children[c];
            p->sum += inc;
        }
    }
    
    int sum(string prefix) {
        TrieNode *p = root.get();
        for (auto c : prefix) {
            if (!p->children[c]) {
                return 0;
            }
            p = p->children[c];
        }
        return p->sum;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */