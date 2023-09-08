// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = []
    
    def read(self, buf: List[str], n: int) -> int:    
        copied, readchar = 0, 4
        if n == 0:
            return 0
        for i in range(len(self.buffer)):
            if i < n and self.buffer[i] != " ":
                buf[copied] = self.buffer[i]
                copied += 1
        if copied == n:
            self.buffer = self.buffer[copied:]
            return copied
        
        buf4 = [" "] * 4
        while copied <= n and readchar == 4:
            print(self.buffer)
            readchar = read4(buf4)
            self.buffer.extend(buf4)
            for i in range(readchar):
                if copied == n:
                    self.buffer = self.buffer[copied:]
                    return copied
                buf[copied] = buf4[i]
                copied += 1
        self.buffer = self.buffer[copied:]
        return copied