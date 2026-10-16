import pandas as pd
from fastapi import FastAPI
import joblib


from schema import  Record
from database import  connection

model=joblib.load("Heart_diseases_model.pkl")
# print(model.feature_names_in_)
app=FastAPI()

@app.get("/")
def get():
    return {
        "message":"heart disease predictive model running"
    }

@app.post("/predict")
def post(data:Record):

    input_data =data.model_dump()

    update=pd.DataFrame([input_data])

    predict=model.predict(update)[0]



    con=connection()
    cursor=con.cursor()

    query=""" INSERT INTO heart_predictive_data (Age,Gender,Impluse,pressure_high,
    pressure_low,Glucose,Potassium,Troponin,result)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);

    """

    cursor.execute(
        query,(data.Age,data.Gender,data.Impluse,data.pressurehigh,data.pressurelow,data.Glucose,
               data.Potassium,data.Troponin,predict)
    )

    con.commit()
    cursor.close()
    con.close()

    return {
        'message': predict
    }