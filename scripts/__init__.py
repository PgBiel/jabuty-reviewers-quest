import os
import sys


def _execute(*args, inherit_args=True) -> None:
    if inherit_args:
        args = (*args, *sys.argv[1:])
    print(f"-- Script: running '{' '.join(args)}' --")
    os.execvp(args[0], args)


backend_src_dir = "reviewers_quest"


# Runs the app.
def run() -> None:
    _execute("python", backend_src_dir + "/app.py")


# Formats the backend code.
def format() -> None:
    _execute("poetry", "run", "ruff", "format", backend_src_dir)


# Checks the backend code.
def check() -> None:
    _execute("poetry", "run", "ruff", "check", backend_src_dir)

# Regenerates the database.
# CAUTION: leads to LOSS OF DATA.
def regendb() -> None:
    from reviewers_quest.regendb import regen_db
    print("-- Script: regenerating database --")
    regen_db()
