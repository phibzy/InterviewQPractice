#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Feb 22, 2021 11:54:30 AEDT
  @file        : shortestPath

"""

from collections import deque

class Solution1:
    def shortestPathLength(self, graph):
        # One approach (brute forcy):
        """
        Pure Brute force
        
        Dijkstra's from every starting position
        Use set to keep track of visited positions
        
        Early exit if next smallest path is already greater than weight of
        current shortest path
        
        Way to mark dead ends? Use hash
        
        """
        
        # Conidition for one node graph or one edge graph
        # Optimal path will either be itself or one node to the next
        # node
        if len(graph) <= 2:
            return len(graph) - 1
        
        shortestWeight = float('inf')
        
        for i in range(len(graph)):
            q = deque()
            # print(''.rjust(10, '-'))
            # print(f"Starting from node {i}")
            # print(''.rjust(10, '-'))
            # print()
            # print()
            
            # Append starting index, weight, path taken and starting visited set
            q.append((i, 0, dict(), set([i])))
            
            # Keep going until we have a path that's visited
            # all nodes
            while True:
                # print(''.rjust(10, '*'))
                # print("Next iteration")
                # print(f"Current q: {q}")
                # print(''.rjust(10, '*'))
                # print()

                n, weight, deadEnds, seen = q.popleft()
                numDead = 0
                # print(f"Currently at node: {n}")
                
                # If next smallest path is greater than current
                # shortest path length, no point continuing
                if weight >= shortestWeight: break
                    
                # Add current node to set
                seen.add(n)
                
                # If visited every node, we can stop this check
                if len(seen) == len(graph):
                    shortestWeight = weight
                    break
                
                # Add to dead ends if we've reached end of a direction
                if len(graph[n]) == 1:
                    deadEnds[n] = 1

                # If only one option that's not a dead end, then
                # this node also becoomes a dead end
                numDead = len([x for x in graph[n] if x in deadEnds])

                if len(graph[n]) - numDead == 1:
                    deadEnds[n] = 1
                    
                for neighbour in graph[n]:
                    if neighbour not in deadEnds:
                        self.addToQ(neighbour, weight + 1, deadEnds.copy(), seen.copy(), q)
                
        return shortestWeight
            
    def addToQ(self, n, w, d, seen, q):
        k = 0
        
        while k < len(q) and q[k][1] <= w:
            k += 1
            
        q.insert(k, (n, w, d, seen))        


    """

    Better approach:

    We can use a BFS (since no weights), which guarantees our q is always in order.
    We can also use a visited hash.
    Since we're only concerned about visiting all nodes, we will use a set
    to keep track of our "state" for each path. We stop searching once we have a state
    which has seen all nodes.

    With our visited hash, instead of checking whether we visited somewhere, we check 
    whether we visited somewhere with THE SAME STATE. For example, could have taken a different path there 
    and visited different nodes on the way.

    """

class Solution:
    def shortestPathLength(self, graph):
        # Still have the same condition checking for < 2 edges
        if not graph: return 0
        if len(graph) <= 2: return len(graph) - 1

        minWeight = float('inf')

        # Still start from different nodes

        # Update: Instead of repeating from different start points,
        # just add each start point/state to q!
        # Also means we don't have to keep track of weight

        # q for BFS
        nextQ = deque([(i, 1 << i) for i in range(len(graph))])

        # For visited, we want to create N dictionaries
        # keeping track of states that have visited particular nodes
        # So we have one for each node, using state as key
        visited = [ {i: 1 << i} for i in range(len(graph))  ] 

        # print("".rjust(10, '-'))
        # print(f"New starting node {i}, with state {bin(visited[i])}")
        steps = 0

        # print("".rjust(10, '-'))
        while True:
            # By using two queues, we can keep track of the depth
            # level using a steps variable, and increment each time
            # the q storing the next level is empty
            q = nextQ

            # Reset q for next level
            nextQ = deque()

            # Same as before
            while q:
                node, state = q.popleft()

                # DON'T NEED THIS ANYMORE
                # If the next lowest weight we check is greater or equal
                # to our current minWeight, we won't find a better
                # path from this starting node
                # if weight >= minWeight: break

                # Add next node to state
                # OR it with 1 shifted left N bits
                state |= (1 << node) 

                # If we've visited all nodes, we're donezo
                # A fully 1'd state can be found by bit shifting
                # 1 by the number of nodes, then subtracting 1
                completeState = ((1 << (len(graph))) - 1)
                if state == completeState:
                    return steps

                # Otherwise, keep checking for path
                for neighbour in graph[node]:
                    # If we have already visited a node
                    # with the same state, don't add to q 
                    if not (state in visited[neighbour]):
                        nextQ.append((neighbour, state))

                # This doesn't help, since we want to keep track of ALL STATES
                # which have visited a node
                visited[node][state] = 1

            steps += 1

