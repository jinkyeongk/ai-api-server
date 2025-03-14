import pickle
from typing import Union
from fastapi import FastAPI
# model.py 가져옴

import model


app = FastAPI()

# 모델 저장 경로
MODEL_PATH = "saved_model.pkl"

model = model.AndModel()

@app.get("/")
def read_root():
    #딕셔너리를 반환하면 JSON으로 응답한다.
    return {"Hello": "World"} 

#/items/{item_id} 경로
# item_id 경로 매개변수(파라메터)
@app.get("/items/{item_id}") # EendPoint
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/predict/left/{left}/right/{right}")
def predict(left: int, right : int):
    result = model.predict([left, right])
    return {"result": result }


@app.post("/train")
def train():
    model.train()
    return {"result": "OK"}

@app.post("/save")
def save():
    # 파일로 저장
    with open('saved_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return {"Saved": "OK"}


@app.post("/load")
def load():
    global model  # ✅ FastAPI 앱의 글로벌 model 변수 사용
    with open('saved_model.pkl', 'rb') as f:
        model = pickle.load(f)
        return {"Loaded": "OK"}
    
