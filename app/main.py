from fastapi import FastAPI
from nicegui import ui, app as nicegui_app
from app.database import create_db_and_tables
from app.config_manager import init_config
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup():
    create_db_and_tables()
    init_config()

# Import routers
from app.routers import grades, config, upload, results, ai_tips, pages

# Mount NiceGUI
nicegui_app.mount("/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)