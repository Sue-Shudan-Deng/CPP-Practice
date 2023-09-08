// https://leetcode.com/problems/word-ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS，重点是通过创建all_combo这个dict来剪枝，否则需要像花花那样遍历所有字母
        """
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
                    if visited.get(w, False):
                        continue
                    if not visited.get(w, False):
                        # 注：这里step和visited可以合并
                        visited[w] = True
                        queue.append((w, step + 1))
                # 这里的作用是为了剪枝省时间，可以不写
                all_combo[word[:i] + '*' + word[i+1:]] = []
        return 0
    
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         """
#         双向BFS
#         """
#         # 前面这几行都是一样的
#         if not beginWord or not endWord or not wordList or endWord not in wordList:
#             return 0
#         all_combo = collections.defaultdict(list)
#         L = len(beginWord)
#         for word in wordList:
#             for i in range(L):
#                 all_combo[word[:i] + '*' + word[i+1:]].append(word)
#         visited_start = {beginWord: 1}
#         visited_end = {endWord: 1}
        
#         # Queues for birdirectional BFS
#         queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
#         queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord
        
#         def visitWordNode(queue, visited, others_visited):
#             word, step = queue.popleft()
#             for i in range(L):
#                 for w in all_combo[word[:i] + '*' + word[i+1:]]:
#                     if others_visited.get(w, 0):
#                         return step + others_visited[w] 
#                     if w == word or visited.get(w, 0):
#                         continue
#                     if not visited.get(w, 0):
#                         # 注：这里step和visited可以合并
#                         visited[w] = step + 1
#                         queue.append((w, step + 1))
#             return None
        
#         # 这里建立两个queue是因为同时对两个方向BFS
#         # 如果有一个方向的queue变成空，那么说明该方向BFS已经结束，并且不可能到达
#         while queue_begin and queue_end:
#             ans = visitWordNode(queue_begin, visited_start, visited_end)
#             if ans:
#                 return ans
#             ans = visitWordNode(queue_end, visited_end, visited_start)
#             if ans:
#                 return ans
#         return 0