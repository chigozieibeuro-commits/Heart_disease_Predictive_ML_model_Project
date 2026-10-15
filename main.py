import pandas as pd
from fastapi import FastAPI
import joblib


from schema import  Record
from database import  connection

model=joblib.load("Heart_diseases_model.pkl")

app=FastAPI()

@app.get("/")
def get():
    return {
        "message":"heart disease predictive model running"
    }

@app.post("/predict")
def post(data:Record):

    input_data=data.model_dump()

    update=pd.DataFrame([input_data])

    predict=model.predict(update)[0]



    con=connection()
    cursor=con.cursor()

    query=""" INSERT INTO heart_disease_predictive_data(Age,Gender,Impluse,pressure_high,
    pressure_low,Glucose,Potassium,Troponin)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
    
    """

    cursor.execute(
        query,(data.age,data.age,data.gender,data.impulse,data.pressure_high,data.pressure_low,data.glucose,
               data.glucose,data.potassium,data.Troponin)
    )

    con.commit()
    con.close()
    cursor.close()

    return {
        'message': predict
    }