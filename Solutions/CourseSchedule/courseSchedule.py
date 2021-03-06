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
import copy

class Solution:

    def canFinish(self, numCourses, prerequisites):
        if prerequisites == []:              return True
        # if len(prerequisites) >= numCourses: return False

        # # Step 1 - make da graph
        # graph = [[] for _ in range(numCourses)]
        # for i in range(numCourses):
            # graph[i] = [0 for _ in range(numCourses)]


        # # Step 2 - Add edges
        # for x, y in prerequisites:
            # if not (0 <= x < numCourses and 0 <= y < numCourses): return False
            # graph[y][x] = 1
        
        # # print(graph)

        # # Step 3 - do search
        # doneDFS = dict()
        # for x in range(numCourses):
            # if x in doneDFS: continue
            # visited = dict()
            # # If returns false, then we break/return false
            # if not self.dfs(x, numCourses, graph, visited, doneDFS):
                # return False

        # Algo: Make array of indegrees, graph as adj matrix (using hash of ints -> List)
        # Do topological sort, using queue
        graph     = dict() 
        inDegrees = [ 0 for _ in range(numCourses) ]

        for i in range(numCourses):
            graph[i] = list()

        # Add +1 to indegree for node with something pointing to it
        # Add to adjacency lists to represent edges (assuming directed graph)
        for x, y in prerequisites:
            if not (0 <= x < numCourses and 0 <= y < numCourses): return False
            inDegrees[x] += 1
            graph[y].append(x)


        # Make queue, add all 0 indegree nodes to queue
        q = list()

        for i, val in enumerate(inDegrees):
            if val == 0:
                q.append(i)

        count = 0
        while q:
            # Take node out of queue, subtract from indegree of neighbours, then add neighbours if indegree = 0
            # Keep track of count too - if we don't service all nodes in queue then there is a cycle
            nextNode = q.pop(0)
            count += 1

            #For each neighbour
            for n in graph[nextNode]:
                inDegrees[n] -= 1
                if inDegrees[n] == 0:
                    q.append(n)


        return count == numCourses


    def dfs(self, x, numCourses, graph, visited, doneDFS):
        # Problem with algo - check if it visits origin? But that's wrong since you could get cycle elsewhere
        if x in visited: return False
        if x in doneDFS: return True

        # For future reference, in a problem like this with unique integers in a given range - use an array for visited
        visited[x] = True
        doneDFS[x] = True
        # pdb.set_trace()

        for i in range(numCourses):
            if graph[x][i] == 1:
                if not self.dfs(i, numCourses, graph, copy.deepcopy(visited), doneDFS):
                    return False

        return True


"""
Graph implementation tradeoffs:
    - Adj Matrix: O(V^2) space complexity, but constant access time
    - Adj List:   O(V+E) space complexity, but worst case access time of O(E)

    Some cases e.g. if E is way bigger than V, then matrix might be good idea

"""


# a = Solution()
# print(a.canFinish(5, [[1,0],[2,1],[3,1],[4,2],[4,3]]))
