from pydantic import BaseModel


class Record(BaseModel):
    Age:int
    Gender:str
    Impluse:int
    pressurehigh:int
    pressurelow:int
    Glucose:int
    Potassium:float
    Troponin:float


