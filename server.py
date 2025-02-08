from fastapi import FastAPI
from routes.auth import router as auth_routers
from routes.supplier import router as supplier_routers
from routes.collector import router as collector_routers


app = FastAPI()


app.include_router(supplier_routers)
app.include_router(auth_routers)
app.include_router(collector_routers)



@app.get("/")
async def root():
    return {"message": "Hello World"}


