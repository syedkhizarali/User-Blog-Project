from fastapi import FastAPI
from user_database.db import engine                                                                        , Base
from routes import user_routes,uploads,posts

app = FastAPI(title="User-Blog-APiI")

Base.metadata.create_all(bind=engine)
app.include_router(user_routes.router)
app.include_router(uploads.router)
app.include_router(posts.router)