#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="../templates")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Path: {}".format(path))
    return render_template("vue/index.html")

def main():
    app.run()

if __name__ == '__main__':
    main()
