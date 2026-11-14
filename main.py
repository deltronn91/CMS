from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from database import Base, engine
import models 

from routes import router

#creates a table(s) in my dbs using my models
#because models are of type BASE/sql alchemy ORM (transfer b/w python and SQL)
Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")