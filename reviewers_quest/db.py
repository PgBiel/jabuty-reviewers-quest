"""Database operations."""

import os
import typing
import sqlalchemy as sql
from .app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_sqlalchemy.model import Model as SqlModel
from typing import TypeAlias

db_path: str = os.path.abspath(os.environ.get("JABRQ_DATABASE", default="database.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_path)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db: SQLAlchemy = SQLAlchemy(app)
BaseModel: TypeAlias = typing.cast(type[SqlModel], db.Model)


def model_to_dict(instance: BaseModel) -> dict:
    """
    Converts the given model to a dictionary with its attributes.

    :param instance: The model instance to convert to a dictionary.
    :return: The converted dictionary.
    """
    return {col.key: getattr(instance, col.key) for col in sql.inspect(instance).mapper.column_attrs}


class Game(BaseModel):
    """Represents a game in the database."""

    game_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(256))
    release_year = sql.Column(sql.Integer)
    developer = sql.Column(sql.String(256), nullable=True)
    publisher = sql.Column(sql.String(256), nullable=True)

    # note: the value of 'func.now()' will be determined by SQLite on insertion.
    created_at = sql.Column(sql.DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"Game(id={self.game_id}, name={self.name})"
