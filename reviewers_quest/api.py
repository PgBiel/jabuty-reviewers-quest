"""API routes for the frontend to interact with."""
import typing

from .app_def import app
from .db import Game, model_to_dict
from flask import abort


def register_api() -> None:
    """Registers the API routes."""
    print("API routes registered.")


@app.route("/api/games/<int:game_id>")
def get_game(game_id: int) -> dict:
    """
    Returns information about a game upon GET.

    :param game_id: ID of the game to obtain info from.
    :return: Information about this game, or 404 if there's no game with that ID.
    """
    return model_to_dict(Game.query.get_or_404(game_id, "Jogo não encontrado"))


@app.route("/api/", defaults={"path": ""})
@app.route("/api/<path:path>")
def api_catch_all(_path: str) -> typing.Never:
    """For unknown API routes, always responds with a 404."""
    abort(404, description="No such API endpoint")
