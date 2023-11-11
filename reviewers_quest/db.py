"""Database operations."""

import os
import sqlalchemy as sql
from .app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db_path: str = os.path.abspath(os.environ.get("JABRQ_DATABASE", default="database.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_path)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db: SQLAlchemy = SQLAlchemy(app)


class Game(db.Model):
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
