// https://leetcode.com/problems/evaluate-division

class Solution {
    
private:
    pair<string, double>& find(string node, map<string, pair<string, double>>& parent) {
        if (node != parent[node].first) {
            auto& p = find(parent[node].first, parent);
            parent[node].first = p.first;
            parent[node].second *= p.second;
        }
        return parent[node];
    }
    
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        map<string, pair<string, double>> parent;
        for (auto i = 0; i < equations.size(); ++i) {
            auto e = equations[i];
            const string& u = e[0]; 
            const string& v = e[1];
            const double k = values[i];
            if (!parent.count(u) && !parent.count(v)) {
                // second node as parent
                parent[u] = {v, k};
                parent[v] = {v, 1.0};
            } else if (!parent.count(u)) {
                // second node as parent
                parent[u] = {v, k};
            } else if (!parent.count(v)) {
                // first node as parent
                parent[v] = {u, 1 / k};
            } else {
                // [["a","b"],["e","f"],["b","e"]]
                auto& pu = find(u, parent);
                auto& pv = find(v, parent);
                parent[pu.first] = {pv.first, k / pu.second * pv.second};
            }
        }
        
        vector<double> ans;
        for (const auto& pair : queries) {
            const string& X = pair[0];
            const string& Y = pair[1];
            if (!parent.count(X) || !parent.count(Y)) {
                ans.push_back(-1.0);
                continue;
            }
            auto& rX = find(X, parent); // {rX, X / rX}
            auto& rY = find(Y, parent); // {rY, Y / rY}
            if (rX.first != rY.first)
                ans.push_back(-1.0);
            else // X / Y = (X / rX / (Y / rY))
                ans.push_back(rX.second / rY.second);
        }
        return ans;
    }
};