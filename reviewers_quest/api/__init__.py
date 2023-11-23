"""Registers API endpoints."""
import typing

from flask import abort

from .game import register_game_api
from .user import register_user_api
from ..app_def import app


def register_api() -> None:
    """Registers the API routes."""

    register_game_api()
    register_user_api()
    print("API routes registered.")


@app.route("/api/", defaults={"path": ""})
@app.route("/api/<path:path>")
def api_catch_all(_path: str) -> typing.Never:
    """For unknown API routes, always responds with a 404."""
    abort(404, description="No such API endpoint")
