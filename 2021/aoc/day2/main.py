#!/usr/bin/python3


class day2:
    def __init__(self):
        self.test_file = open("./test", "r")
        self.test_list = self.ToList(self.test_file)

        self.input_file = open("./input", "r")
        self.input_list = self.ToList(self.input_file)

        self.input_result = list()

    def task1(self):
        sel_list = self.input_list
        horizontal = 0
        depth = 0
        for steer in sel_list:
            key, value = steer.split(" ")
            value = int(value)
            if key == "forward":
                horizontal += value
            elif key == "down":
                depth += value
            elif key == "up":
                depth -= value
        print("=" * 12)
        print(f"horizontal: {horizontal}\ndepth: {depth}")
        print(horizontal * depth)

    def task2(self):
        sel_list = self.input_list
        horizontal = 0
        depth = 0
        aim = 0
        for steer in sel_list:
            key, value = steer.split(" ")
            value = int(value)
            if key == "forward":
                horizontal += value
                depth += aim * value
            elif key == "down":
                # depth += value
                aim += value
            elif key == "up":
                # depth -= value
                aim -= value
        print("=" * 12)
        print(f"horizontal: {horizontal}\ndepth: {depth}\naim: {aim}")
        print(horizontal * depth)

    def ToList(self, input: list[int]) -> list[int]:
        return [(x.strip()) for x in input]


d1 = day2()

# d1.task1()
d1.task2()
"""
a 0
f 5
-
d 5
a 5
f 8 +5 = 13
since a =5, and f=8, d=8*5=40

u 3
"""
