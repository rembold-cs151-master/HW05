# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os

import Prob1
import Prob2
import Prob3

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def test_docstring_A(self):
        assert len(Prob1.Part_A.__doc__.strip()) > 0, 'No docstring found'
    def test_docstring_B(self):
        assert len(Prob1.Part_B.__doc__.strip()) > 0, 'No docstring found'
    def test_docstring_C(self):
        assert len(Prob1.Part_C.__doc__.strip()) > 0, 'No docstring found'


class Test_Prob2:
    # ep = 0.001
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_births(self):
        args = [(2,4), (11,4), (7,3)]
        sols = [4,20,9]
        for i,a in enumerate(args):
            student = Prob2.births(*a)
            assert student == sols[i], self.report(a)

    def test_rabbit_pop(self):
        args = [10, 2, 4]
        sols = [108000, 18, 160]
        for i,a in enumerate(args):
            student = Prob2.rabbit_pop(a)
            assert student == sols[i], self.report(a)

    # def test_rabbit_pop_wolf(self):
        # args = [(10,2), (5,5), (2,5)]
        # sols = [100706, 394, 15]
        # for i,a in enumerate(args):
            # student = Prob2.rabbit_pop_w_wolves(*a)
            # assert student == sols[i], self.report(a)

    def test_rabbit_pop_wolf_new(self):
        args = [(10,2), (5,5), (2,5)]
        sols = [37800, 140, 10]
        sols2 = [54942, 151, 11]
        for i,a in enumerate(args):
            student = Prob2.rabbit_pop_w_wolves(*a)
            assert student == sols[i] or student == sols2[i], self.report(a)

    def test_rabbit_pop_wolf_int(self):
        args = (10,2)
        student = Prob2.rabbit_pop_w_wolves(*args)
        assert type(student) == int, 'You are not returning an integer!'

    def test_needed_num_wolves(self):
        student = Prob2.calc_needed_wolves()
        assert student == 7 or student == 8


class Test_Prob3:
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
            student = Prob3.is_flush(a)
            assert student == sols[i], self.report(a)


    def test_count_flushes(self):
        student = Prob3.count_flushes('hands.txt')
        assert student == 6

    def test_count_flushes_output(self):
        Prob3.count_flushes('hands.txt')
        with open('flushes.txt', 'r') as f:
            lines = f.readlines()
        assert len(lines) == 6, 'Incorrect number of lines in the output file'

