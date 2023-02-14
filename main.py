from fastapi import FastAPI, Body
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root_get():
    return RedirectResponse(url="/static/index.html")


@app.post("/oil")
async def root_post(a=Body(embed=True), b=Body(embed=True), c=Body(embed=True),
                    d=Body(embed=True)):  # параметры без валидации
    prediction, probability = oil_advicer(a, b, c, d)
    print(prediction, probability)
    return {"message": f" Предсказание - {prediction}, Вероятность - {probability.round(3)}%."}


def oil_advicer(a, b, c, d):  # Передаются: плотность деэмульгатора -a (т/м3); кинематическая вязкость - b (мм2/с);
    # массовая доля активного вещества - c (%); плотность нефти - d (т/м3).
    label = {0: 'Плохой деэмульгатор', 1: 'Хороший деэмульгатор'}

    X = np.array([[a, b, c, d]])
    advicer = pickle.load(open(os.path.join('static/clf.pkl'), 'rb'))
    prediction = label[advicer.predict(X)[0]]
    probability = np.max(advicer.predict_proba(X)) * 100
    return [prediction, probability]


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
