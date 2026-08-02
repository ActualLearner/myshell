#!/bin/python3
import os
import sys
from collections import defaultdict

fns = defaultdict()
fns["cd"] = os.chdir
fns["exit"] = sys.exit


def find_file(filename):
    dirs = os.environ.get("PATH").split(":")

    for dir in dirs:
        if os.path.exists(dir) and filename in os.listdir(dir):
            return f"{dir}/{filename}"

    raise (FileNotFoundError("Program Not Found."))


def execute(data):
    if data[0] in fns:
        arg = " ".join(data[1:]).strip()
        fn = fns[data[0]]
        fn(arg)
        return

    pid = os.fork()
    if pid > 0:
        os.wait()
    else:
        try:
            path = find_file(data[0])
        except FileNotFoundError:
            os._exit(1)

        os.execv(path, data)
