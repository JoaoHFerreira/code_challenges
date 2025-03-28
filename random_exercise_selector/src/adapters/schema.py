from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class CodeChallengesTable(Base):
    __tablename__ = "code_challenges"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    exercise_name = Column(String, nullable=False)
    exercise_description = Column(String, nullable=False)
    golang = Column(Boolean, nullable=False, server_default="0")
    lualang = Column(Boolean, nullable=False, server_default="0")
    elixirlang = Column(Boolean, nullable=False, server_default="0")
    rustlang = Column(Boolean, nullable=False, server_default="0")


class ChallengesTracker(Base):
    __tablename__ = "challenges_tracker"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    code_challenge_id = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    start_date = Column(DateTime(timezone=True), server_default=func.now())
    end_date = Column(DateTime(timezone=True), nullable=True)
