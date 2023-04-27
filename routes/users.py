from fastapi import APIRouter
from config.db import conn
from models.index import applicants
from schemas.index import User
user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(applicants.select()).fetchall()

@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(applicants.select().where(applicants.c.id==id)).fetchall()

@user.get("/")
async def write_data(user: User):
     conn.execute(applicants.insert().values(
        name=user.name,
        email=user.email_id
    ))
     return conn.execute(applicants.select()).fetchall()

@user.put("/{id}")
async def update_data(id:int, user:User):
    conn.execute(applicants.update().values(
        name=user.name,
        email=user.email_id
    ).where(applicants.c.id==id))
    return conn.execute(applicants.select()).fetchall()

@user.delete("/")
async def delete_data():
    conn.execute(applicants.delete().where(applicants.c.id==id))
    return conn.execute(applicants.select()).fetchall()

@user.get("/")
async def read_data():
    return conn.execute(applicants.select()).fetchall()
