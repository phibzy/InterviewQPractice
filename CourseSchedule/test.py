#!/usr/bin/python3

"""
Cases:
    - No prereqs
    - More or equal prereqs to courses
    - Prereq of itself
    - Out of bounds course
    - Normal long prereq list
    - Two paths to course on prereq tree
    - Isolated course
    - One course, at least one prereq

"""
from courseSchedule import Solution
import unittest

class testCourseSchedule(unittest.TestCase):

    a = Solution()

    def testNoPrereq(self):
        self.assertTrue(self.a.canFinish(2, []), "Error: Fails 0 prereq test")

    def testMorePrereqThanCourse(self):
        self.assertTrue(self.a.canFinish(4, [[1,0],[2,1],[3,2],[3,0]]), "Error: Fails redundant prereq case")

    def testOutOfBoundsCourse(self):
        self.assertFalse(self.a.canFinish(4, [[1,0],[2,4],[5,2],[3,-1]]), "Error: Fails out of bounds course case")

    def testPrereqOfItself(self):
        self.assertFalse(self.a.canFinish(5, [[1,0],[2,4],[2,2],[5,3]]), "Error: Fails prereq of itself case")

    def testTwoPathsToOneCourse(self):
        self.assertTrue(self.a.canFinish(5, [[1,0],[2,1],[3,1],[4,2], [4,3]]), "Error: Fails two path case")

    def testTwoPathsDifferentOrigins(self):
        self.assertTrue(self.a.canFinish(6, [[1,0],[2,1], [3,2],[5,4], [5,3]]), "Error: Fails two paths, different origins case")

    def testNormalLongPrereqCourse(self):
        self.assertTrue(self.a.canFinish(9, [[1,0],[2,1],[3,2],[4,2],[5,3],[6,3],[7,4],[8,7]]), "Error - fails long prereq course case")

    def testOneCoursePrereqItself(self):
        self.assertFalse(self.a.canFinish(1, [[0,0]]), "Error: Fails prereq of itself case (1 course)") 

    def testOneCourseAtLeastOnePrereq(self):
        self.assertFalse(self.a.canFinish(1, [[1,0]]), "Error: Fails prereq for 1 course case") 

    def testIsolatedCourses(self):
        self.assertTrue(self.a.canFinish(12, [[1,0],[2,1],[3,2],[4,2],[5,3],[6,3],[7,4],[8,7]]), "Error - fails isolated courses case")


