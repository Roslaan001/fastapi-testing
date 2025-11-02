from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi, This is Roslaan deploying this FastAPI application from Pipeops!"}