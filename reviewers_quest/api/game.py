"""/api/game routes."""
from flask import request

from ..app_def import app
from ..db import Game, model_to_dict


def register_game_api() -> None:
    """Registers the game API routes."""

    print("Game API routes registered.")


@app.route("/api/games")
def get_games() -> list[dict]:
    """Gets a list of games."""
    name_filter = request.args.get("filter", default="")
    amount = request.args.get("amount", default=50, type=int)

    games = Game.query.filter(Game.name.ilike(f"%{name_filter}%")).limit(amount).all()
    return [game_to_dict(game) for game in games]


@app.route("/api/game/<int:game_id>")
def get_game(game_id: int) -> dict:
    """
    Returns information about a game upon GET.

    :param game_id: ID of the game to obtain info from.
    :return: Information about this game, or 404 if there's no game with that ID.
    """
    return game_to_dict(Game.query.get_or_404(game_id, "Jogo não encontrado"))


@app.route("/api/game/<int:game_id>/reviews")
def get_reviews(game_id: int) -> list[dict]:
    """
    Returns a list of reviews for this game.

    :param game_id: ID of the game to obtain reviews for.
    :return: List of reviews for that game.
    """
    game: Game = Game.query.get_or_404(game_id, "Jogo não encontrado")
    return [
        model_to_dict(review, keys=("review_id", "game_id", "author_id", "stars", "body")) for review in game.reviews
    ]


def game_to_dict(game: Game) -> dict:
    """
    Converts a Game instance to a dict with properties exposed by the API.

    :param game: The game to convert to a dict.
    :return A dictionary with the public properties of Game.
    """
    return model_to_dict(
        game,
        keys=("game_id", "name", "image", "release_year", "publisher", "developer", "genre"),
    )
