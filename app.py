from fake_data_app import create_app
from fastapi import FastAPI

store_dict = create_app()

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
