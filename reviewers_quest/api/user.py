"""/api/user routes."""
from flask import flash, make_response, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.wrappers.response import Response

from ..app_def import app
from ..db import User, db


def register_user_api() -> None:
    """Registers the User API routes."""

    print("User API routes registered.")


@app.route("/api/user/login", methods=["POST"])
def login_post() -> Response:
    """Endpoint to log in as a user."""

    # login code goes here
    email = request.form.get("email")
    password = request.form.get("password") or ""
    remember = bool(request.form.get("remember"))

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("login"))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return make_response("Success", 200)


@app.route("/api/user", methods=["POST"])
def signup_post() -> Response:
    """Endpoint to create a user."""

    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password") or ""

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


@app.route("/api/user/logout")
@login_required
def logout() -> Response:
    """Endpoint to logout from the current user session."""
    logout_user()
    return make_response("Success", 200)
