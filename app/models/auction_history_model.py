from sqlalchemy import Column, String, Integer, ForeignKey
from app.core.database import Base

class AuctionHistory(Base):
    """
    Stores the auction history for each player and team per year.
    """
    __tablename__ = "auction_history"

    auction_id = Column(String(10), primary_key=True, unique=True, nullable=False)  # Prefixed with SLAA
    player_id = Column(String(10), ForeignKey("players.player_id"), nullable=False)
    team_id = Column(String(10), ForeignKey("teams.team_id"), nullable=False)
    year = Column(String(10), nullable=False)
    sold_price = Column(Integer, nullable=False)
    base_price = Column(Integer, nullable=False)  # Added as per schema decision
