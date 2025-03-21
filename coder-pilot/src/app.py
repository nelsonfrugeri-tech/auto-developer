import uvicorn
from fastapi import FastAPI
from src.router.router import main_router

app = FastAPI(title="multi-agent-api", description="MultiAgent API")
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=8080, reload=True)
