# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob1
import Prob2
import Prob3

extra_credit = pytest.mark.skipif(Prob3.autochecks == False, reason="Unattempted extra credit")

class Test_Prob1:
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
            assert student == sols[i], f"is_flush is giving {student} for is_flush({a}) but the answer is {sols[i]}."


    def test_count_flushes(self):
        student = Prob1.count_flushes('hands.txt')
        assert student == 6, f"count_flushes('hands.txt') should have output 6 but instead output {student}."

    def test_count_flushes_output(self):
        Prob1.count_flushes('hands.txt')
        with open('hands_flushes.txt', 'r') as f:
            lines = f.readlines()
        assert len(lines) == 6, f'You are supposed to output one hand per line in the output file, so I would expect 6 lines but am reading {len(lines)}.'

class Test_Prob2:
    def test_file_puzzles(self):
        puzzles = Prob2.get_puzzles("puzzles.txt")
        sols = [True] * 5 + [False] * 5
        for i in range(len(puzzles)):
            student = Prob2.is_valid_puzzle(puzzles[i])
            assert student == sols[i], f"Puzzle {i} should return {sols[i]} but you are returning {student}."



class Test_Prob3:
    ml_sols = [[-1, 1, 0, 0, 2, -1], [3, 3, 2, 1, 4, -1], [-1, -1, 2, -1, 3, -1], [-1, 4, 3, 2, 2, 1], [1, 2, -1, 1, 0, 0], [0,
1, 1, 1, 0, 0]] 

    alt_layout1 = [[True, True, False],[False, True, True], [False, False, False]]
    alt1_sols = [[-1, -1, 3], [3, -1, -1], [1, 2, 2]]

    alt_layout2 = [[True, True, False],[False, True, True]]
    alt2_sols = [[-1, -1, 3], [3,-1,-1]]

    @extra_credit
    def test_check_index_location(self):
        to_check = [[0,0], [5,5], [3,0], [0,3]]
        for point in to_check:
            student = Prob3.check_index_location(*point, Prob3.mine_locations)
            thissol = self.ml_sols[point[0]][point[1]]
            assert student == thissol, f"Should have returned {thissol} but instead returned {student} with inputs of check_index_location({*point, Prob3.mine_locations})."

    @extra_credit
    def test_count_mines_returns_proper_sized_array(self):
        to_check = [Prob3.mine_locations, self.alt_layout1, self.alt_layout2]
        sols = [[6,6],[3,3], [2,3]]
        for array,sizes in zip(to_check, sols):
            student = Prob3.count_mines(array)
            assert len(student) == sizes[0], "Array seems to be the wrong height?"
            assert len(student[0]) == sizes[1], "Array seems to be the wrong width?"
    @extra_credit
    def test_count_mines_returns_correct_counts(self):
        to_check = [Prob3.mine_locations, self.alt_layout1, self.alt_layout2]
        sols = [self.ml_sols, self.alt1_sols, self.alt2_sols]
        for array, sol in zip(to_check, sols):
            student = Prob3.count_mines(array)
            assert student == sol, f"count_mines({array}) is giving {student} but it should be {sol}."
