#!/usr/bin/python3
""" import module"""


import sys


def read_stdin(to_dict, file_size):
    """
    reads stdin line by line and computes metrics:
    """

    print("File size: {}".format(file_size))
    for key, value in sorted(to_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


file_size = 0
code = 0
counter = 0
to_dict = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    while True:
        read_line = sys.stdin.readline()
        if not read_line:
            break

        parsed_line = read_line.split()  # trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in to_dict.keys()):
                    to_dict[code] += 1

            if (counter == 10):
                read_stdin(to_dict, file_size)
                counter = 0

finally:
    read_stdin(to_dict, file_size)
