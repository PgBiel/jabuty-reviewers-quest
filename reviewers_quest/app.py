#!/usr/bin/env python3

from .app_def import app
from flask import render_template



@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def frontend_catch_all(path: str) -> str:
    print(f"Path: {path}")
    return render_template("vue/index.html")


def main() -> None:
    app.run()


if __name__ == "__main__":
    main()
