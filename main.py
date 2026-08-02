#!/bin/python3
from execute import execute
from parser import parse
import os
import socket

while True:
    device_info = f"\033[92m{os.environ.get('USER')}@{socket.gethostname()}"
    path_info = f"\033[94m~{os.getcwd()}\033[0m"
    string = device_info + ":" + path_info + "$ "

    try:
        user_input = input(string)
    except KeyboardInterrupt:
        print()
        continue

    try:
        parsed_data = parse(user_input)
    except Exception as e:
        print("Error parsing", e)
        continue

    try:
        execute(parsed_data)
    except OSError as e:
        print("Error executing commnd", e)
