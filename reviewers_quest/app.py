#!/usr/bin/env python3

from flask import render_template
from flask_login import LoginManager

from .app_def import app
from .api import register_api
from .db import User

register_api()


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def frontend_catch_all(path: str) -> str:
    """Catch all route for the frontend (Vue has its own internal router)."""
    print(f"Path: {path}")
    return render_template("vue/index.html")


def main() -> None:
    """Main function, starts the Flask app."""

    app.config["SECRET_KEY"] = "reviewers-quest-secret-key"

    login_manager = LoginManager()
    login_manager.login_view = "login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: int) -> User:
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    app.run()


if __name__ == "__main__":
    main()
