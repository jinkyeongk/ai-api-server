from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

import practice.app_model as app_model
import practice.chat_model as chat_model
import sql_chat_model



app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

model = sql_chat_model.TranslationModel()


@app.get("/translates")
def translate(text: str = Query(), language: str = Query(default="ko"), session_id: str = Query(default="default_thread")):
    response = model.translate( text, language, session_id)
    return {"content" :response}
