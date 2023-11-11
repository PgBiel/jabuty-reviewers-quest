"""Defines the application and any accompanying global variables."""

from flask import Flask

app = Flask(__name__, static_folder="../static", template_folder="../templates")
