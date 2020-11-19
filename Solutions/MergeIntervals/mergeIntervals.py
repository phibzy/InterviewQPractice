#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Nov 19, 2020 11:33:31 AEDT
  @file        : mergeIntervals

"""

class Solution:
    def merge(self, intervals):
        # if there's only one interval there's no merging to be done
        if len(intervals) < 2: return intervals

        # Algo: Sort based on start, end of each interval
        # then iterate through comparing with next element,
        # modifying endpoint of current element if they need to be merged
        # + deleting next element, otherwise leaving them both as is

        # TC: O(NlogN) - Sort list (NlogN), then make one pass of list (N)
        # SC: O(1)     - We merge the intervals in place

        # Sort list based on start of interval, then end of interval if equal
        intervals.sort(key= lambda x: (x[0], x[1]))

        i = 0
        while (i+1) < len(intervals):
            # check for overlap
            # because it's sorted we only need to check if the
            # start of the next interval lies in the current interval
            if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1]:
                
                # if the end of next element is greater than end of current one,
                # we widen the length of current interval to equal it
                if intervals[i+1][1] > intervals[i][1]:
                    intervals[i][1] = intervals[i+1][1]

                # Otherwise the next interval lies inside the current one,
                # so we can just delete it.
                del intervals[i+1]

            # Otherwise no overlap, move on to next comparison
            # We don't increment if we deleted an element
            else:
                i += 1

        return intervals

