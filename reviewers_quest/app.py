#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path: str) -> str:
    print(f"Path: {path}")
    return render_template("vue/index.html")


def main() -> None:
    app.run()


if __name__ == "__main__":
    main()
