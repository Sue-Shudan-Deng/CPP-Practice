// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        status = ["unk" for _ in range(numCourses)]
        for p, q in prerequisites:
            graph[q].append(p)
            
        def dfs(node):
            """
            whether or not can form a circle
            if starting from this node
            """
            if status[node] == "visited":
                return False
            if status[node] == "visiting":
                return True
            status[node] = "visiting"
            for nei in graph[node]:
                if dfs(nei):
                    return True
            status[node] = "visited"
            return False
            
        for node in range(numCourses):
            if dfs(node):
                return False
        return True