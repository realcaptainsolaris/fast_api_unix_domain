from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
async def get_data():
    return {"message": "Hello from Service B!"}
