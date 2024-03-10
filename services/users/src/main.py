import uvicorn
from fastapi import FastAPI
from api import router

app = FastAPI(
    title="Users Service",
    description="This is a simple users service.",
    version="0.0.1",
    redoc_url=None,
    openapi_url="/api/v1/openapi.json",
)

app.include_router(router)


@app.get("/ping")
def ping():
    return {"ping": "pong!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
