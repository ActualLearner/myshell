# Myshell -- A Python Shell From Scratch

## Introduction

In the age of AI, it is more important than ever to keep our skills from atrophying. Days of AI-assisted coding can turn into weeks, and months without us realising that we haven't touched code in a while. I made this project to refresh my coding skills, and my architectural thinking, as well as to see what python has to offer in regards to lower level programming(sys calls, etc). I chose python for this one, and I'll probably use C++ for the next project(Docker from scratch) and I'll keep alternating.

## File Structure

Three files:

- main.py:
  The entry point that runs while True loop, accepts input, calls the parse to parse the user input, then calls execute on it.
- parser.py:
  Responsible for parsing user input, filling in variables(env variables as well), and cleaning the input from white space.
- execute.py:
  The main execution happens here. It accepts the input parsed by `parser.py`, and then searches for the executables in all directories specified in the PATH environmental variable as is standard in shells. It then forks the current process. The parent waits for the child to finish executing before continuing to accept user input. The child uses a helper function `find_file` to find the executable location, and uses the exec system call to run it.

## Explanations

- System call:
  The main way for interacting with the kernel. Read [here](https://www.geeksforgeeks.org/operating-systems/introduction-of-system-call/)
