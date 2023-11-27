"""Database operations."""

import os
import typing
from typing import TypeAlias

import sqlalchemy as sql
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model as SqlModel
from sqlalchemy import func, orm

from .app import app

db_path: str = os.path.abspath(os.environ.get("JABRQ_DATABASE", default="database.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_path)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db: SQLAlchemy = SQLAlchemy(app)
BaseModel: TypeAlias = typing.cast(type[SqlModel], db.Model)


def model_to_dict(instance: BaseModel) -> dict:
    """
    Converts the given model to a dictionary with its attributes.

    Excludes 'created_at' by default.

    :param instance: The model instance to convert to a dictionary.
    :return: The converted dictionary.
    """
    return {
        col.key: getattr(instance, col.key)
        for col in sql.inspect(instance).mapper.column_attrs
        if col.key != "created_at"
    }


class Game(BaseModel):
    """Represents a game in the database."""

    game_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(256))
    release_year = sql.Column(sql.Integer)
    developer = sql.Column(sql.String(256), nullable=True)
    publisher = sql.Column(sql.String(256), nullable=True)
    reviews: orm.Mapped[list["Review"]] = orm.relationship()

    # note: the value of 'func.now()' will be determined by SQLite on insertion.
    created_at = sql.Column(sql.DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"Game(id={self.game_id}, name={self.name})"


class User(UserMixin, BaseModel):
    """Represents a user which can log into the website."""

    user_id = sql.Column(sql.Integer, primary_key=True)
    email = sql.Column(sql.String(100), unique=True)
    password = sql.Column(sql.String(100))
    name = sql.Column(sql.String(1000))
    created_at = sql.Column(sql.DateTime(timezone=True), server_default=func.now())
    reviews: orm.Mapped[list["Review"]] = orm.relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.user_id}, name={self.name})"


class Review(BaseModel):
    """Represents a user's review on a specific game."""

    review_id = sql.Column(sql.Integer, primary_key=True)
    game_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Game.game_id))
    author_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(User.user_id))
    stars = sql.Column(sql.Integer, sql.CheckConstraint("stars >= 0 AND stars <= 5"))
    body = sql.Column(sql.String(100))
    user: orm.Mapped[User] = orm.relationship(back_populates="reviews")

    def __repr__(self) -> str:
        return (
            f"Review(review_id={self.review_id}, game_id={self.game_id}, author_id={self.author_id}, "
            f"stars={self.stars}, body={self.body})"
        )
