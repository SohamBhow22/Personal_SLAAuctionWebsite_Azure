from pydantic import BaseModel

class AdminBase(BaseModel):
    username: str

class AdminCreate(AdminBase):
    password: str  # Accepts plain text, but will be hashed

class AdminResponse(AdminBase):
    admin_id: str

    class Config:
        orm_mode = True
