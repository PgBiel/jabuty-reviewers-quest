"""Database operations."""

import os
import typing
from collections.abc import Collection
from typing import TypeAlias

import sqlalchemy as sql
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model as SqlModel
from sqlalchemy import func, orm

from .app_def import app

db_path: str = os.path.abspath(os.environ.get("JABRQ_DATABASE", default="database.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_path)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db: SQLAlchemy = SQLAlchemy(app)
BaseModel: TypeAlias = typing.cast(type[SqlModel], db.Model)


def model_to_dict(instance: BaseModel, *, keys: Collection[str] | None = None) -> dict:
    """
    Converts the given model to a dictionary with its attributes.

    Excludes 'created_at' by default.

    :param instance: The model instance to convert to a dictionary.
    :param keys: The keys to include in the dict, or None for all (bar 'created_at').
    :return: The converted dictionary.
    """
    return {
        col.key: getattr(instance, col.key)
        for col in sql.inspect(instance).mapper.column_attrs
        if (keys is not None and col.key in keys) or (keys is None and col.key != "created_at")
    }


class Game(BaseModel):
    """Represents a game in the database."""

    game_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(256), nullable=False)
    image = sql.Column(sql.String(256), nullable=False)
    release_year = sql.Column(sql.Integer, nullable=False)
    developer = sql.Column(sql.String(256), nullable=False)
    publisher = sql.Column(sql.String(256), nullable=False)
    genre = sql.Column(sql.String(256), nullable=False)
    reviews: orm.Mapped[list["Review"]] = orm.relationship()

    # note: the value of 'func.now()' will be determined by SQLite on insertion.
    created_at = sql.Column(sql.DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"Game(game_id={self.game_id}, name={self.name})"


class User(UserMixin, BaseModel):
    """Represents a user which can log into the website."""

    user_id = sql.Column(sql.Integer, primary_key=True)
    email = sql.Column(sql.String(100), unique=True, nullable=False)
    password = sql.Column(sql.String(100), nullable=False)
    name = sql.Column(sql.String(1000), nullable=False)
    bio = sql.Column(sql.String(10000), nullable=True)
    interests = sql.Column(sql.String(100), nullable=True)
    created_at = sql.Column(sql.DateTime(timezone=True), server_default=func.now(), nullable=False)
    reviews: orm.Mapped[list["Review"]] = orm.relationship(back_populates="user")

    def get_id(self) -> int:
        """Overrides UserMixin's get_id. Returns the user's ID."""
        return typing.cast(int, self.user_id)

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id}, name={self.name})"


class Review(BaseModel):
    """Represents a user's review on a specific game."""

    review_id = sql.Column(sql.Integer, primary_key=True)
    game_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Game.game_id), nullable=False)
    author_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(User.user_id), nullable=False)
    stars = sql.Column(sql.Integer, sql.CheckConstraint("stars >= 0 AND stars <= 5"), nullable=False)
    body = sql.Column(sql.String(100), nullable=False)
    user: orm.Mapped[User] = orm.relationship(back_populates="reviews")

    def __repr__(self) -> str:
        return (
            f"Review(review_id={self.review_id}, game_id={self.game_id}, author_id={self.author_id}, "
            f"stars={self.stars}, body={self.body!r})"
        )
