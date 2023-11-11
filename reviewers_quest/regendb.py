from .app import app
from .db import db


def regen_db() -> None:
    """
    Regenerates the database.

    CAUTION: This will DELETE THE EXISTING DATA.
    ONLY RUN THIS IN DEBUG. DO NOT RUN IN PRODUCTION.
    """
    with app.app_context():
        print("[!] Dropping existing database...")
        db.drop_all()
        print("[!] Creating new database...")
        db.create_all()


if __name__ == "__main__":
    regen_db()
