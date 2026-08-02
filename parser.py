#!/bin/python3
import os


def parse(data):
    temp = data.split(" ")
    arr = []

    for item in temp:
        if not item:
            continue

        if item[0] == "$":
            var = os.environ.get(item[1:])
            if var:
                arr.append(var)

            continue

        arr.append(item)

    return arr
