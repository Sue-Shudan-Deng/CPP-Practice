// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        这类题可归类为子部分顺序翻转
        做法是全局reverse + 部分reverse
        方法1: build-in
        注意join的用法：(a: str).join(b: List), 
        a将成为b各个子部分之间连接的关节
        """
        return "".join(reversed(s.split()))
    

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        方法2: 全局翻转 + 部分翻转
        """
        # Step1: trim the spaces
        def trim(s: str):
            lo, hi = 0, len(s) - 1
            while lo <= hi and s[lo] == ' ':
                lo += 1
            while lo <= hi and s[hi] == ' ':
                hi -= 1
            
            output = []
            while lo <= hi:
                if s[lo] != ' ':
                    output.append(s[lo])
                elif output[-1] != ' ':  # 这一步极其巧妙
                    output.append(s[lo])
                lo += 1
            return output
        
        # Step2: reverse function 
        def reverse(l: list, left: int, right: int):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right - 1
                
        # Step3: reverse each word
        def reverse_each_word(l: list) -> None:
            """
            双指针
            """
            lo, hi = 0, 0
            n = len(l)
            
            while lo < n:
                while hi < n and l[hi] != ' ':
                    hi += 1
                reverse(l, lo, hi - 1)
                lo = hi + 1  # 需要+1是因为有个空格
                hi += 1
            
        l = trim(s)
        reverse(l, 0, len(l) - 1)
        reverse_each_word(l)
        return "".join(l)
    
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        方法三: 用deque
        原因: 主要是因为可以appendleft
        """
        lo, hi = 0, len(s) - 1
        
        while lo <= hi and s[lo] == ' ':
            lo += 1
        while lo <= hi and s[hi] == ' ':
            hi -= 1
        
        end = lo
        queue, word = collections.deque(), []
        while end <= hi:
            if s[end] != ' ':
                word.append(s[end])
            elif word:
                queue.appendleft("".join(word))
                word = []
            end += 1
        queue.appendleft("".join(word))
        return " ".join(queue)