import sys
import subprocess

def _execute(*args, exit=True, inherit_args=True):
    if inherit_args:
        args = (*args, *sys.argv[1:])
    print(f"-- Script: running '{' '.join(args)}' --")
    try:
        returncode = subprocess.run(args).returncode
        if exit:
            sys.exit(returncode)
    except KeyboardInterrupt:
        if exit:
            sys.exit(0)
        raise
    except:
        if exit:
            sys.exit(1)
        raise

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
