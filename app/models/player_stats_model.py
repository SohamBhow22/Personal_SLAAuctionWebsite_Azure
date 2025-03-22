from sqlalchemy import Column, String, Integer, ForeignKey
from app.core.database import Base

class PlayerStats(Base):
    """
    Stores performance stats for players per year.
    """
    __tablename__ = "player_stats"

    stats_id = Column(String(10), primary_key=True, unique=True, nullable=False)  # Prefixed with SLAS
    player_id = Column(String(10), ForeignKey("players.player_id"), nullable=False)
    year = Column(String(10), nullable=False)
    matches_played = Column(Integer, default=0, nullable=False)
    runs_scored = Column(Integer, default=0, nullable=False)
    wickets_taken = Column(Integer, default=0, nullable=False)
