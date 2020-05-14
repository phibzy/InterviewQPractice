#!/usr/bin/python3

"""
Takes in numCourses(int) and prerequisites (list of list of int) aka graph edges

Returns if possible to finish all courses

Questions to Interviewer:
    - Will there be redundant prereqs? E.g. [[1,0], [2,1], [2,0]]
    - Multiple prereqs?
    - Max numCourses?
    - Range of prereqs size?

Algo:
     If prereqs >= numCourses then impossible to finish all courses
     Make directed graph (adj matrix) of prereqs
     Hash of coords to check if we've visited coord before
     Do DFS/BFS on graph, if you end up at node you already visited, then it's impossible to finish all courses
     Logic: if that happens, then you need to finish course further down the line to do course you've already completed,
            which makes no nense


"""

import pdb

class Solution:

    def canFinish(self, numCourses, prerequisites):
        if prerequisites == []:              return True
        # if len(prerequisites) >= numCourses: return False

        # Step 1 - make da graph
        graph = [[] for _ in range(numCourses)]
        for i in range(numCourses):
            graph[i] = [0 for _ in range(numCourses)]


        # Step 2 - Add edges
        for x, y in prerequisites:
            if not (0 <= x < numCourses and 0 <= y < numCourses): return False
            graph[y][x] = 1
        
        # print(graph)

        # Step 3 - do search
        doneDFS = dict()
        for x in range(numCourses):
            if x in doneDFS: continue
            visited = dict()
            # If returns false, then we break/return false
            if not self.dfs(x, numCourses, graph, visited, doneDFS):
                return False

        return True


    # When working, do an iterative version too
    def dfs(self, x, numCourses, graph, visited, doneDFS):
        # Problem with algo - check if it visits origin? But that's wrong since you could get cycle elsewhere
        if x in visited: return False
        if x in doneDFS: return True
        visited[x] = True
        doneDFS[x] = True

        for i in range(numCourses):
            if graph[x][i] == 1:
                if not self.dfs(i, numCourses, graph, visited, doneDFS):
                    # pdb.set_trace()
                    return False

        return True

a = Solution()
print(a.canFinish(5, [[1,0],[2,1],[3,1],[4,2],[4,3]]))
