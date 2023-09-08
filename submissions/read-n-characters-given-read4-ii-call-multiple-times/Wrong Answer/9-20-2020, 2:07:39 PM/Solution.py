// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = []
    
    def read(self, buf: List[str], n: int) -> int:    
        copied, readchar = 0, 4
        for i in self.buffer:
            if i != " ":
                buf[copied] = i
                copied += 1
        buf4 = [" "] * 4
        while copied <= n and readchar == 4:
            readchar = read4(buf4)
            self.buffer.extend(buf4)
            for i in range(readchar):
                if copied == n:
                    break
                buf[copied] = buf4[i]
                copied += 1
        self.buffer = self.buffer[copied:]
        return copied