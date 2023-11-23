"""API routes for the frontend to interact with."""
import typing

from flask import abort, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from .app_def import app
from .db import Game, User, db, model_to_dict


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


@app.route("/login")
def login():
    return "Login"


@app.route("/login", methods=["POST"])
def login_post():
    # login code goes here
    email = request.form.get("email")
    password = request.form.get("password")
    remember = bool(request.form.get("remember"))

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("login"))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return "LOGIN SUCCESFUL"


@app.route("/signup")
def signup():
    return "Signup"


@app.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email address already exists")
        return redirect(url_for("signup"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "LOGOUT COMPLETE"
