// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        这道题需要认真理解
        """
        graph = collections.defaultdict(list)
        status = ["unk" for _ in range(numCourses)]
        for p, q in prerequisites:
            graph[q].append(p)
            
        def dfs(node, ans):
            """
            whether or not can form a circle if we start from this node
            """
            if status[node] == "visited":
                return True  # True means OK
            if status[node] == "visiting":
                return False # False means CYCLE
            # 所以某种意义上跟backtrack也没任何区别
            # set
            status[node] = "visiting"
            # 这么写是错的！！！这样并不能保证一个节点的所有邻接节点恰好同时在之后被访问
            # ans.append(node)
            for nei in graph[node]:
                if not dfs(nei, ans):
                    return False
            # clear
            status[node] = "visited"
            # 重点！！！！！这样写才可能保障每个节点的邻接节点恰好位于该节点前！！！
            ans.append(node)
            return True
            
        ans = []
        for node in range(numCourses):
            if not dfs(node, ans):
                return []
        return ans[::-1] # 重点！！逆序输出！！！