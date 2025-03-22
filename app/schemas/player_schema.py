from pydantic import BaseModel

class PlayerBase(BaseModel):
    player_name: str
    mobile_number: str
    address: str
    stumps_id: str | None = None

class PlayerResponse(PlayerBase):
    player_id: str

    class Config:
        orm_mode = True
