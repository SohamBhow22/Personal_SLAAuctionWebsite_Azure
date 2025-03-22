from sqlalchemy import Column, String
from app.core.database import Base

class Player(Base):
    """
    Represents a player participating in the auction.
    """
    __tablename__ = "players"

    player_id = Column(String(10), primary_key=True, unique=True, nullable=False)  # Prefixed with SLAP
    player_name = Column(String(100), nullable=False)
    mobile_number = Column(String(15), unique=True, nullable=False)
    address = Column(String(4), nullable=False)
    stumps_id = Column(String(20), unique=True, nullable=True)  # Optional unique ID
