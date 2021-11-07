from datetime import date as date_
from datetime import datetime
from pydantic import BaseModel


class CreateData(BaseModel):
    date: date_


class Createuser(BaseModel):
    name: str
    wm_latitude: int
    wm_longitude: int
    token: str
    propId: int
    exchangeCoinNumber: int
    pushPlusToken: str

class ReadData(CreateData):
    name: str
    wm_latitude: int
    wm_longitude: int
    token: str
    propId: int
    exchangeCoinNumber: int
    pushPlusToken: str
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True


class Readuser(Createuser):
    name: str
    wm_latitude: int
    wm_longitude: int
    token: str
    propId: int
    exchangeCoinNumber: int
    pushPlusToken: str
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode =  True