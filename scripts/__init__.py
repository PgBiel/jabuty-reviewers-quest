import os
import sys


def _execute(*args, inherit_args=True) -> None:
    if inherit_args:
        args = (*args, *sys.argv[1:])
    print(f"-- Script: running '{' '.join(args)}' --")
    os.execvp(args[0], args)


backend_src_dir = "reviewers_quest"


# Runs the app.
def run() -> None:
    _execute("python", "-m", backend_src_dir)


# Formats the backend code.
def format() -> None:
    _execute("poetry", "run", "ruff", "format", backend_src_dir)


# Checks the backend code.
def check() -> None:
    _execute("poetry", "run", "ruff", "check", backend_src_dir)


# Runs mypy to typecheck Python code.
def typecheck() -> None:
    _execute("poetry", "run", "mypy", "-p", backend_src_dir)


# Populates the database with sample data.
def populatedb() -> None:
    print("-- Script: Populating the database with sample data --")
    from reviewers_quest.app_def import app
    from reviewers_quest.db import db, Game, User, Review

    with app.app_context():
        session = db.session()
        game1 = Game(
            name="Outer Wilds",
            image="https://image.api.playstation.com/vulcan/ap/rnd/202208/1623/Zofebh60Ue7Zt5sC10UAtU3D.png",
            release_year=2019,
            developer="Mobius Digital",
            publisher="Annapurna Digital",
            genre="Mistério",
        )
        game2 = Game(
            name="Celeste",
            image="https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg?t=1701122042",
            release_year=2018,
            developer="Extremely OK Games, Ltd.",
            publisher="Maddy Makes Games Inc.",
            genre="Plataforma",
        )

        user1 = User(
            name="John Unexistent",
            email="john@not.exist.com",
            password="lol-you-cant-log-in-as-john",
            bio="I'm John.",
            interests="Mistério",
        )

        user2 = User(
            name="Mary Unexistent",
            email="mary@not.exist.com",
            password="lol-you-cant-log-in-as-mary",
            bio="I'm Mary.",
            interests="Plataforma",
        )

        print(f"Creating games: {game1.name!r}, {game2.name!r}")
        print(f"Creating users: {user1.name!r}, {user2.name!r}")
        session.add(game1)
        session.add(game2)
        session.add(user1)
        session.add(user2)
        session.commit()

        review1 = Review(
            game_id=game1.game_id,
            author_id=user1.user_id,
            stars=4,
            body="Legal, mas não encontrei nenhuma bola de futebol no jogo.",
        )
        review2 = Review(
            game_id=game1.game_id, author_id=user2.user_id, stars=5, body="Excelente, simplesmente perfeito."
        )

        print(f"Creating 2 reviews for game #{review1.game_id}")
        session.add(review1)
        session.add(review2)
        session.commit()


# Regenerates the database.
# CAUTION: leads to LOSS OF DATA.
def regendb() -> None:
    from reviewers_quest.regendb import regen_db

    print("-- Script: regenerating database --")
    regen_db()
