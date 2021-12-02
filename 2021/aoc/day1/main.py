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

    def task2(self):
        sel_inp = self.input_list
        window_sum = 0
        count_dracula = []
        print(sel_inp)
        for idx in range(0, len(sel_inp), 1):
            _slice = sel_inp[idx : idx + 3]
            if len(_slice) == 3:
                window_sum = sum(_slice)
                count_dracula.append(window_sum)
                print(f"{_slice=} = {window_sum}")
        try:
            for idx, elem in enumerate(count_dracula):
                if elem < count_dracula[idx + 1]:
                    self.input_result.append(1)

                elif elem > count_dracula[idx + 1]:
                    self.input_result.append(0)
        except IndexError as e:
            ...
        print(sum(self.input_result))

    # [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    #   A    A    A
    #        B    B    B

    def ToList(self, input: list[int]) -> list[int]:
        return [int(x.strip()) for x in input]


d1 = day1()

# (d1.task1())
# print("=" * 12)
# if sum(d1.input_result) == 1399:
#    print(1400)
#  det var ikke slik på part2, feelsbadman ;_;

d1.task2()
