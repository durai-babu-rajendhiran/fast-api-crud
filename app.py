from fastapi import FastAPI
import uvicorn

from routes.User import router as user_router
from routes.Item import router as main_router

app = FastAPI()
app.include_router(main_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)