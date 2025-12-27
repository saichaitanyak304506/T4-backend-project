from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import tools, reviews, admin

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Tool Finder Backend")

@app.get("/")
def greet():
    return {"message": "Welcome to Backend Project!!!"}

app.include_router(tools.router)
app.include_router(reviews.router)
app.include_router(admin.router)
