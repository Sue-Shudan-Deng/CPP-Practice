// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        status = ["unk" for _ in range(numCourses)]
        for p, q in prerequisites:
            graph[q].append(p)
            
        def dfs(node):
            """
            whether or not can form a circle if we start from this node
            """
            if status[node] == "visited":
                return True
            if status[node] == "visiting":
                return False # False means CYCLE
            status[node] = "visiting"
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            status[node] = "visited"
            return True
            
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        