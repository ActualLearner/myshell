#!/bin/python3
import os
import sys

fns = {}
fns["cd"] = os.chdir
fns["exit"] = sys.exit


def find_file(filename):
    dirs = os.environ.get("PATH").split(":")

    for dir in dirs:
        if os.path.exists(dir) and filename in os.listdir(dir):
            return f"{dir}/{filename}"

    raise (FileNotFoundError("Program Not Found."))


def execute_one(data, r, w):

    if data[0] in fns:
        arg = " ".join(data[1:]).strip()
        fn = fns[data[0]]
        try:
            fn(arg)
        except OSError:
            raise
        return

    pid = os.fork()
    if pid > 0:
        if w:
            os.close(w)
        return pid
    else:
        try:
            path = find_file(data[0])
        except FileNotFoundError:
            os._exit(1)

        if w:
            os.dup2(w, sys.stdout.fileno())
            os.close(w)
        if r:
            os.dup2(r, sys.stdin.fileno())
            os.close(r)

        os.execv(path, data)


def execute_all(arr):

    prev_r = None
    pids = []

    for i, data in enumerate(arr):
        r, w = os.pipe()

        if i == len(arr) - 1:
            os.close(w)
            w = None

        pid = execute_one(data, prev_r, w)
        prev_r = r
        if pid:
            pids.append(pid)

    for pid in pids:
        os.waitpid(pid, 0)

    if prev_r:
        os.close(prev_r)
