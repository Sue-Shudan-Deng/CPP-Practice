// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0   # 当前的数字
        curr = ""  # 当前正在处理的字符串
        
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char) # 因为数字本身不一定是个位数，所以不能直接取int 
            elif char == '[':
                stack.append(curr)
                stack.append(num)
                curr = "" # 清空当前正在处理的字符串，设置为开始处理
                num = 0  # 因为数字暂时用不上了所以清0
                print(stack)
            elif char == ']':
                # 说明当前小范围的string已经处理完了，那么需要去整理下当前的string
                cnt = int(stack.pop()) # 这里的stack的状态大致是: ["", '2', 'a', '3', 'bca', '4']
                pre_str = stack.pop()
                curr = pre_str + cnt * curr
                # new current string
            else:
                curr += char
        return curr