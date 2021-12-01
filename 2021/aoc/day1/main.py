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
        try:
            for idx, elem in enumerate(sel_list):
                if elem < sel_list[idx + 1]:
                    print(f"{elem} < {sel_list[idx + 1]}")
                    self.input_result.append(1)
                    print(f"{elem} (increased)")

                elif elem > sel_list[idx + 1]:
                    print(f"{elem} > {sel_list[idx + 1]}")
                    self.input_result.append(0)
                    print(f"{elem} (decreased)")

        except IndexError as e:
            ...

    def ToList(self, input: list[int]) -> list[int]:
        return [(x.strip()) for x in input]


d1 = day1()

(d1.task1())
print("=" * 12)
if sum(d1.input_result) == 1399:
    print(1400)
