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
    return model_to_dict(Game.query.get_or_404(game_id, "Jogo não encontrado"))
