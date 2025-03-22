from sqlalchemy import Column, String
from app.core.database import Base

class Team(Base):
    """
    Represents a team participating in the auction.
    """
    __tablename__ = "teams"

    team_id = Column(String(10), primary_key=True, unique=True, nullable=False)  # Prefixed with SLAT
    team_name = Column(String(100), unique=True, nullable=False)
    team_leader = Column(String(100), nullable=False)
    team_captain = Column(String(100), nullable=True)
    year_formed = Column(String(10), nullable=False)
