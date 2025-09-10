from fastapi import FastAPI
from app.api.v1 import example

app = FastAPI(
    title="Interview API",
    version="1.0.0",
    description="Boilerplate for interview tasks"
)

# Routers
app.include_router(example.router, prefix="/api/v1/example", tags=["Example"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
