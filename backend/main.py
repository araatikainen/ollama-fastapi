from dotenv import load_dotenv
from fastapi import FastAPI
from api.routes import router

load_dotenv()

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

