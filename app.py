import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from config import settings
from routes.routes import router

app = FastAPI(debug=settings.DEBUG)
app.include_router(router)

Tortoise.init_models(["models"], "models")

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3' if settings.DATABASE_SQLITE else settings.DATABASE_URL,
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000, log_level="info")
