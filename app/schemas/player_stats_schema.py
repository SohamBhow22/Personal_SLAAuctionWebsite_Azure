from pydantic import BaseModel

class PlayerStatsBase(BaseModel):
    player_id: str
    year: str
    matches_played: int = 0
    runs_scored: int = 0
    wickets_taken: int = 0

class PlayerStatsResponse(PlayerStatsBase):
    stats_id: str

    class Config:
        orm_mode = True
