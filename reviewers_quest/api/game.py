"""/api/game routes."""
from ..app_def import app
from ..db import Game, model_to_dict


def register_game_api() -> None:
    """Registers the game API routes."""

    print("Game API routes registered.")


@app.route("/api/game/<int:game_id>")
def get_game(game_id: int) -> dict:
    """
    Returns information about a game upon GET.

    :param game_id: ID of the game to obtain info from.
    :return: Information about this game, or 404 if there's no game with that ID.
    """
    return model_to_dict(
        Game.query.get_or_404(game_id, "Jogo não encontrado"),
        keys=("game_id", "name", "release_year", "publisher", "developer", "genre"),
    )


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
