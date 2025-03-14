from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "connection online"}