#!/usr/bin/python3


class day1:
    def __init__(self):
        self.test_file = open("./test", "r")
        self.test_list = self.ToList(self.test_file)

        self.input_file = open("./input", "r")
        self.input_list = self.ToList(self.input_file)

        self.input_result = list()

    def task1(self):
        sel_list = self.input_list
        ...

    def task2(self):
        sel_list = self.input_list
        ...

    def ToList(self, input: list[int]) -> list[int]:
        return [(x.strip()) for x in input]


d1 = day1()

d1.task1()
d1.task2()
