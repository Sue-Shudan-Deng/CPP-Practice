// https://leetcode.com/problems/word-search-ii

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        # Step 1: build a trie with words
        for w in words:
            node = trie
            for c in w:
                if not c in node:
                    node[c] = {}
                node = node[c]
            # 这一步有点牛逼
            node['#'] = w
            
        # Step 2: backtracking with trie
        matched_words = []
        row, col = len(board), len(board[0])
        
        def backtrack(r, c, parent):
            letter = board[r][c]
            currNode = parent[letter]
            # 这步需要重点理解，非常巧妙
            word_match = currNode.pop('#', False)
            if word_match:
                matched_words.append(word_match)
            board[r][c] = '#'
            for new_r, new_c in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= new_r < row and 0 <= new_c < col and board[new_r][new_c] in currNode:
                    backtrack(new_r, new_c, currNode)
            board[r][c] = letter
            
        for r in range(row):
            for c in range(col):
                if board[r][c] in trie:
                    backtrack(r, c, trie)
                    
        return matched_words