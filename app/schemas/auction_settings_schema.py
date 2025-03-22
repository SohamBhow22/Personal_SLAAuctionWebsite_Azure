from pydantic import BaseModel

class AuctionSettingsBase(BaseModel):
    auction_year: str
    max_players_per_team: int
    base_price_for_year: int
    admin_id: str

class AuctionSettingsResponse(AuctionSettingsBase):
    settings_id: str

    class Config:
        orm_mode = True
