from fastapi import FastAPI, Query

import main

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "connection online"}