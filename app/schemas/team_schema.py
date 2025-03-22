from pydantic import BaseModel

class TeamBase(BaseModel):
    team_name: str
    team_leader: str
    team_captain: str | None = None
    year_formed: str

class TeamResponse(TeamBase):
    team_id: str

    class Config:
        orm_mode = True
