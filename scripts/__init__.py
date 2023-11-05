import os
import subprocess
import sys


def _execute(*args, inherit_args=True):
    if inherit_args:
        args = (*args, *sys.argv[1:])
    print(f"-- Script: running '{' '.join(args)}' --")
    os.execvp(args[0], args)


backend_src_dir = "reviewers_quest"


# Runs the app.
def run():
    _execute("python", backend_src_dir + "/app.py")


# Formats the backend code.
def format():
    _execute("poetry", "run", "ruff", "format", backend_src_dir)


# Checks the backend code.
def check():
    _execute("poetry", "run", "ruff", "check", backend_src_dir)
