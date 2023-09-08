// https://leetcode.com/problems/word-ladder

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        map<string, vector<string>> all_comb;
        map<string, bool> visited;
        int n = beginWord.size();
        for (auto w : wordList) {
            for (int i = 0; i < n; ++i) {
                all_comb[w.substr(0, i) + "*" + w.substr(i+1, n-i-1)].push_back(w);
            }
            visited[w] = false;
        }
        deque<pair<string, int>> q = {{beginWord, 1}};
        
        while (!q.empty()) {
            auto [w, step] = q.front();
            q.pop_front();
            visited[w] = true;
            for (int i = 0; i < n; ++i) {
                for (auto next_w : all_comb[w.substr(0, i) + "*" + w.substr(i+1, n-i-1)]) {
                    if (next_w == endWord) {
                        return step + 1;
                    }
                    if (!visited[next_w]) {
                        q.emplace_back(next_w, step + 1);
                    }   
                }
                all_comb.erase(w.substr(0, i) + "*" + w.substr(i+1, n-i-1));
            }
        }
        return 0;
    }
};