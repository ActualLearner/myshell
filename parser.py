#!/bin/python3
import os


def parse(data):
    temp = data.split(" ")
    arr = []
    curr = []

    for item in temp:
        if not item:
            continue

        if item[0] == "$":
            var = os.environ.get(item[1:])
            if var:
                curr.append(var)

            continue
        elif item == "|":
            arr.append(curr[:])
            curr = []
            continue

        curr.append(item)

    if curr:
        arr.append(curr[:])

    return arr
