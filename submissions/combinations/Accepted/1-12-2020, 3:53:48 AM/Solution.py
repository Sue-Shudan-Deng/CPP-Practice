// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(first: int, curr: List[int]):
            if len(curr) == k:
                res.append(curr[:]) # 这里写成res.append(curr)会报错
            for i in range(first, n + 1):
                curr.append(i) # 置位
                backtrack(i+1, curr) # 回溯
                curr.pop() # 复位
        backtrack(1, [])
        return res
    
"""
a = [1, 2, 3]
b1 = a
b2 = a[:]
b1是a的浅拷贝，即b1和a一样
b2是a的深拷贝，即b2和a不一样

b1和b2的内容和a都是一样的，
但是b1的内存地址和a一样，b2的内存地址和a是不一样的

此处的这个就像按引用传递（b1）和按值传递（b2）
"""
