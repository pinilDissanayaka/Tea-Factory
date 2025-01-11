from fastapi import FastAPI
from routes.auth import router as auth_routers
from routes.user import router as user_routers
from routes.admin import router as admin_routers

app = FastAPI()

app.include_router(auth_routers)
app.include_router(user_routers)
app.include_router(admin_routers)


@app.get("/")
async def root():
    return {"message": "Hello World"}


