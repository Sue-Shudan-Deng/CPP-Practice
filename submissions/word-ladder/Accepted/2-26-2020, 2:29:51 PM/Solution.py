// https://leetcode.com/problems/word-ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        all_combo = collections.defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                all_combo[word[:i] + '*' + word[i+1:]].append(word)
        # if wordList has 6 words and each word has 3 letters, then
        # the size of all_combo is 6*3 = 18
        visited, step = {beginWord: True}, 1
        queue = collections.deque([(beginWord, step)])
        while queue:
            word, step = queue.popleft()
            for i in range(L):
                for w in all_combo[word[:i] + '*' + word[i+1:]]:
                    if w == endWord:
                        return step + 1
                    if w == word or visited.get(w, False):
                        continue
                    if not visited.get(w, False):
                        visited[w] = True
                        queue.append((w, step + 1))
                all_combo[word[:i] + '*' + word[i+1:]] = []
        return 0