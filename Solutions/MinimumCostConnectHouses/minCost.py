#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Feb 20, 2021 17:10:54 AEDT
  @file        : minCost

"""


"""
    Given a 2D array houses[][] consisting of N 2D coordinates {x, y} where
    each coordinate represents the location of each house, the task is to 
    find the minimum cost to connect all the houses of the city.

    We're concerned with Manhattan distances here

    TC: O(N^2) - Create all possible edge combos, sort them by weight, then worst
                 case have to sift through all of them

    SC: O(N^2) - Store all possible edge combos (Each edge has N-1 edges)

"""

def minCost(houses):
    # We're basically looking to find the minimum spanning tree connecting
    # all the houses - we will solve this using Kruskal's algorithm

    # Since we're only caring about the totalWeight, we don't need to reconstruct the graph
    # We will use sets to keep track of which nodes are connected, because
    # we want to avoid creating cycles while ensuring everything remains connected
    # Point at which they connect is fine though

    # If we have less than 2 houses, we will return 0
    if len(houses) < 2: return 0

    # We will create stack of edges, which will be tuples of startpoint, endpoint and weight
    # We will also have an array of sets keeping track of which nodes are connected
    connected = [ set([i]) for i in range(len(houses)) ]
    weights = list()
    
    # What we will return at the end
    minWeight = 0

    i = 0
    while i < len(houses):
        j = i + 1

        while j < len(houses):
            # Calculate man distance or 'weight' of edge
            manDist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])

            # Add to stack, with lightest weight at top
            k = 0
            while k < len(weights) and weights[k][2] > manDist:
                k += 1
            
            # Add tuple consisting of i, j and weight
            weights.insert(k, (i,j,manDist))

            j += 1

        i += 1

    # Alternatively: just add all to list and then sort with weights.sort(key= lambda x: x[2], reverse=True
    # Would give O(NlogN) complexity instead of O(N^2) for insertion sort

    # While everything is not connected
    while len(connected[0]) != len(houses):

        start, end, weight = weights.pop()

        # First, check that each point isn't already connected
        # Can do this by comparing sets
        if end in connected[start] or start in connected[end]: continue

        # Otherwise it's valid, we connect the trees together
        # For every node in union of sets, make their connected set equal to the union
        newSet = connected[start].union(connected[end])
        
        # Because of how Python works, we're not creating N copies of set of size N,
        # but rather having N references pointing to the same set

        # TC for updating sets is O(N), but we do it N times so O(N^2)
        for s in newSet:
            connected[s] = newSet

        # Everytime we add edge to what will be our minimum spanning tree,
        # add its weight to total minWeight
        minWeight += weight

    return minWeight

