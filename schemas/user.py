from pydantic import BaseModel

class User (BaseModel):
    id:int
    name:str
    email_id:str
    phone_no: str