from fastapi import FastAPI
from routes.auth import router as auth_routers


app = FastAPI()

app.include_router(auth_routers)


@app.get("/")
async def root():
    return {"message": "Hello World"}


