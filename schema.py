from pydantic import BaseModel


class Record(BaseModel):
    age:int
    gender:int
    impulse:int
    pressure_high:int
    pressure_low:int
    glucose:int
    potassium:int
    Troponin:int


