from sqlalchemy import create_engine
from src.adapters.schema import Base


def start_engine():
    engine = get_engine()
    Base.metadata.create_all(engine)
    # TODO: Typehints and log
    print("Table created successfully.")


def get_engine(db_path="code-challenges.db"):
    return create_engine(f"sqlite:///{db_path}")
