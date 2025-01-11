from server import app
import uvicorn
from database import engine, Base, session
from models import User

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(app,
                port=8000)
