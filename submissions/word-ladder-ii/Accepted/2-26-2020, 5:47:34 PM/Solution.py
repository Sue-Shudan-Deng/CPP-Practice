// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or not endWord in wordList:
            return []
        L = len(beginWord)
        all_combo = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo[word[:i] + "*" + word[i+1:]].append(word)
        layer = dict()
        layer[beginWord] = [[beginWord]]
        wordSet = set(wordList)
        while layer:
            # 每次都重新创建一个
            newlayer = collections.defaultdict(list)
            for word in layer.keys():
                if word == endWord:
                    return layer[word]
                for i in range(L):
                    newwords = all_combo[word[:i] + "*" + word[i+1:]]
                    for newword in newwords:
                        if newword in wordSet:
                            newlayer[newword] += [j + [newword] for j in layer[word]]
            wordSet -= set(newlayer.keys())
            layer = newlayer
        return []