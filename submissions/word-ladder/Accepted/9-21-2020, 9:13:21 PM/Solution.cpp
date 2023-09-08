// https://leetcode.com/problems/word-ladder

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // BFS
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
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {
            return 0;
        }
        
        visited[beginWord] = true;
        while (!q.empty()) {
            auto [w, step] = q.front();
            q.pop_front();
            for (int i = 0; i < n; ++i) {
                for (auto next_w : all_comb[w.substr(0, i) + "*" + w.substr(i+1, n-i-1)]) {
                    if (next_w == endWord) {
                        return step + 1;
                    }
                    if (!visited[next_w]) {
                        visited[next_w] = true;
                        q.emplace_back(next_w, step + 1);
                    }   
                }
                all_comb.erase(w.substr(0, i) + "*" + w.substr(i+1, n-i-1));
            }
        }
        return 0;
    }
};
    
//     int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
//         // Bidirectional BFS
//         map<string, vector<string>> all_comb;
//         map<string, int> visited_forward;
//         map<string, int> visited_backward;
//         int n = beginWord.size();
//         for (auto w : wordList) {
//             for (int i = 0; i < n; ++i) {
//                 all_comb[w.substr(0, i) + "*" + w.substr(i+1, n-i-1)].push_back(w);
//             }
//         }
//         deque<pair<string, int>> q_forward = {{beginWord, 1}};
//         deque<pair<string, int>> q_backward = {{endWord, 1}};
//         visited_forward[beginWord] = 1;
//         visited_backward[endWord] = 1;
//         string w;
//         int step;
        
//         if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {
//             return 0;
//         }
        
//         while (!q_forward.empty() && !q_backward.empty()) {
//             tie(w, step) = q_forward.front();
//             q_forward.pop_front();
//             for (int i = 0; i < n; ++i) {
//                 for (auto next_w : all_comb[w.substr(0, i) + "*" + w.substr(i+1, n-i-1)]) {
//                     if (visited_backward.count(next_w)) {
//                         cout << "w: " << w << " next_w: " << next_w << endl;
//                         return step + visited_backward[next_w];
//                     }
//                     if (!visited_forward.count(next_w)) {
//                         visited_forward[next_w] = step + 1;
//                         q_forward.emplace_back(next_w, step + 1);
//                     }   
//                 }
//                 // 这里因为双向的做法，剪枝就不太合适了
//                 // all_comb.erase(w.substr(0, i) + "*" + w.substr(i+1, n-i-1));
//             }
            
//             tie(w, step) = q_backward.front();
//             q_backward.pop_front();
//             for (int i = 0; i < n; ++i) {
//                 for (auto next_w : all_comb[w.substr(0, i) + "*" + w.substr(i+1, n-i-1)]) {
//                     if (visited_forward.count(next_w)) {
//                         return step + visited_forward[next_w];
//                     }
//                     if (!visited_backward.count(next_w)) {
//                         visited_backward[next_w] = step + 1;
//                         q_backward.emplace_back(next_w, step + 1);
//                     }   
//                 }
//             }
//         }
//         return 0;
//     }
// };