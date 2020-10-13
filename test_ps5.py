# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest
import os

import Prob1
import Prob2

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_is_flush(self):
        args = [
                "TH 4H AH JH 8H",
                "TH 4D AS JH TS",
                "2D 3D 4D AD 8D",
                "AS 2S 3S 4S 5C",
                ]
        sols = [True, False, True, False]
        for i,a in enumerate(args):
            student = Prob1.is_flush(a)
            assert student == sols[i], self.report(a)


    def test_count_flushes(self):
        student = Prob1.count_flushes('hands.txt')
        assert student == 6

    def test_count_flushes_output(self):
        Prob1.count_flushes('hands.txt')
        with open('hands_flushes.txt', 'r') as f:
            lines = f.readlines()
        assert len(lines) == 6, 'Incorrect number of lines in the output file'


class Test_Prob2:
    ml_sols = [[-1, 1, 0, 0, 2, -1], [3, 3, 2, 1, 4, -1], [-1, -1, 2, -1, 3, -1], [-1, 4, 3, 2, 2, 1], [1, 2, -1, 1, 0, 0], [0,
1, 1, 1, 0, 0]] 
    alt_layout1 = [[True, True, False],[False, True, True], [False, False, False]]
    alt1_sols = [[-1, -1, 2], [3, -1, -1], [1, 2, 2]]
    alt_layout2 = [[True, True, False],[False, True, True]]
    alt2_sols = [[-1, -1, 3], [3,-1,-1]]
    
    def test_check_index_location(self):
        to_check = [[0,0], [5,5], [3,0], [0,3]]
        for point in to_check:
            student = Prob2.check_index_location(*point, Prob2.mine_locations)
            thissol = self.ml_sols[point[0]][point[1]]
            assert student == thissol, f"Should have returned {thissol} but instead returned {student}"

    def test_count_mines_returns_proper_sized_array(self):
        to_check = [Prob2.mine_locations, self.alt_layout1, self.alt_layout2]
        sols = [[5,5],[3,3], [2,3]]
        for array,sizes in zip(to_check, sols):
            student = Prob2.count_mines(array)
            assert len(student) == sizes[0], "Array seems to be the wrong height?"
            assert len(student[0]) == sizes[1], "Array seems to be the wrong width?"

    def test_count_mines_returns_correct_counts(self):
        to_check = [Prob2.mine_locations, self.alt_layout1, self.alt_layout2]
        sols = [self.ml_sols, self.alt1_sols, self.alt2_sols]
        for array,sol in zip(to_check, sols):
            student = Prob2.count_mines(array)
            assert student == sol, f"Array of counts seems to be off, as {sols} was expected but you returned {student}"
