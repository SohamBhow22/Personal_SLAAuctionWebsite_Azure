from fastapi import FastAPI
from app.core.config import engine
from app.models import player_model, team_model

app = FastAPI()

# Ensure tables are created
player_model.Base.metadata.create_all(bind=engine)
team_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to SLA Auction API!"}