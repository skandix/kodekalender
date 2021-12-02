#!/usr/bin/python3
import pandas

# https://pypi.org/project/pygeoif/


class day1:
    def __init__(self):
        self.input_file = pandas.read_csv("./cities.csv")
        self.input_list = self.ToList(self.input_file)

    def task1(self):
        for loc in self.input_file["location"]:
            print(loc)

    def ToList(self, input: list[int]) -> list[int]:
        return [(x.strip()) for x in input]


d1 = day1()
(d1.task1())
