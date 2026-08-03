# MyShell -- A Python Shell From Scratch

## Introduction

In the age of AI, it is more important than ever to keep our skills from atrophying. Days of AI-assisted coding can turn into weeks, and months without us realising that we haven't touched code in a while. I made this project to refresh my coding skills, and my architectural thinking, as well as to see what python has to offer in regards to lower level programming(sys calls, etc). I chose python for this one, and I'll probably use C++ for the next project(Docker from scratch) and I'll keep alternating.

## File Structure

Three files:

- main.py:
  The entry point that runs while True loop, accepts input, calls the parse to parse the user input, then calls execute on it.
- parser.py:
  Responsible for parsing user input, filling in variables(env variables as well), and cleaning the input from white space. Returns a list of each command and it's arguments (separates them by pipes).
- execute.py:
  The main execution happens here. It accepts the input parsed by `parser.py`, and for each command, it searches for its executable in all directories specified in the PATH environmental variable as is standard in shells. It then iterates over each command, forks and runs them with execv, and collects the pids and waits for them all to finish. It also creates read and write file descriptors, for each child process, and passes the child process the prev read fd and the current write fd (if it's the first command) to handle piping. The child uses a helper function `find_file` to find the executable location, and uses the os.execv to run it.

## Explanations

- System call:
  The main way for interacting with the kernel. Read [here](https://www.geeksforgeeks.org/operating-systems/introduction-of-system-call/)
- fork:
  The system call that creates a new copy of the current process. Done by calling os.fork() which returns the pid of the child to the parent process, and returns pid of 0 to the child process.
- exec:
  The system call that runs the process or executable specified in it's arguments. The new process replaces the process that calls it. Done by calling os.execv() and passing two arguments: a string of the path to the executable and list of its arguments.

- File Descriptors:
  Are file representations of resources in computers. A file descriptor can be opened, closed, copied(copies are opened and closed separately), etc.
- Pipe:
  Two file descriptors whose contents are collected such that the read fd allows reading, while the write fd allows writing to it.
- Builtins:
  Are builtin functions that cannot be forked due to the behaviour of the action they take. Eg: cd can't be forked and executed because it acts on the current process itself, and needs a parent/outside process to actually perform that action on it.
