#!/usr/bin/python3
import requests

from num2words import num2words

class day1:
    def __init__(self):
        self.session = requests.get
        self.input_file = (
            self.session(
                "https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBNdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--0af4f790dec929a13e3615fdac11667323ea1597/tall.txt?disposition=inline"
            )
            .text.encode("ISO-8859-1")
            .decode()
        )
        self.input_list = self.ToList(self.input_file)

    def task1(self):
        print(self.input_file)

    def ToList(self, input: list[int]) -> list[int]:
        return [(x.strip()) for x in input]


d1 = day1()
(d1.task1())
