// https://leetcode.com/problems/unique-word-abbreviation

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.m = {}
        for s in dictionary:
            if len(s) <= 2:
                self.m[s] = 1
            else:
                key = s[0]+str(len(s) - 2)+s[-1]
                self.m[key] = 1

    def isUnique(self, word: str) -> bool:
        if len(word) > 2:
            word = word[0] + str(len(word) - 2) + word[-1]
        return not self.m.get(word, 0)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)