// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        status = ["unk" for _ in range(numCourses)]
        for p, q in prerequisites:
            graph[q].append(p)
            
        def dfs(node):
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
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            # clear
            status[node] = "visited"
            return True
            
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        