from pydantic import BaseModel

class AuctionHistoryBase(BaseModel):
    player_id: str
    team_id: str
    year: str
    sold_price: int
    base_price: int

class AuctionHistoryResponse(AuctionHistoryBase):
    auction_id: str

    class Config:
        orm_mode = True
