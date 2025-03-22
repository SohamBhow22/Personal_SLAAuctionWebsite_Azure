from sqlalchemy import Column, String, Integer, ForeignKey
from app.core.database import Base

class AuctionSettings(Base):
    """
    Stores auction settings such as max players per team and base price.
    """
    __tablename__ = "auction_settings"

    settings_id = Column(String(10), primary_key=True, unique=True, nullable=False)  # Prefixed with SLAX
    auction_year = Column(String(10), unique=True, nullable=False)
    max_players_per_team = Column(Integer, nullable=False)
    base_price_for_year = Column(Integer, nullable=False)
    admin_id = Column(String(10), ForeignKey("admins.admin_id"), nullable=False)  # Added as per schema decision
