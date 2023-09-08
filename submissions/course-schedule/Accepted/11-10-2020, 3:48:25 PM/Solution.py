// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        visited = set()
        visiting = set()
        for p, q in prerequisites:
            graph[q].append(p)
            
        def dfs(node):
            """
            whether or not can form a circle if we start from this node
            """
            if node in visited:
                return True
            if node in visiting:
                return False # False means CYCLE
            # set
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            # clear
            visiting.remove(node)
            visited.add(node)
            return True
            
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        