#uvicorn main:app --reload
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import mysql.connector
from fastapi import (    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status,
)
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# adding cors urls
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Job Application database</h1>

    </body>
</html>
"""
while True:
    try:
        conn = mysql.connector.connect(host = 'localhost', port = 3306,
                                    username = 'root', password = 'Sanskar1234',
                                    database = 'job_application_system')
        cursor = conn.cursor(dictionary=True)

        print("Successfully connected to database")
        break
    except Exception as error:
        print("Error connecting to database")
        print("Error", error)
        break

class Application(BaseModel):
    name: str
    age: int
    email_id: str
    phone_no: str
    cgpa: float
    college: str
    skill: str

@app.get("/")
def root():
    return HTMLResponse(html)

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")

@app.get("/users")
def get_user():
    cursor.execute("SELECT * FROM applicants")
    user = cursor.fetchall()
    return user

@app.post("/users", status_code= status.HTTP_201_CREATED)
def create_user(usr : Application):
    cursor.execute("""INSERT INTO applicants(name, age, email_id, phone_no,cgpa, college, skill) VALUES(%s,%s,%s,%s,%s,%s,%s)""",(usr.name, usr.age, usr.email_id, usr.phone_no,usr.cgpa, usr.college, usr.skill))
    cursor.execute("SELECT * FROM applicants ORDER BY id DESC LIMIT 1")
    new_user = cursor.fetchone()
    conn.commit()
    return {'data': new_user}

@app.get("/users/{id}")
def get_user(id:int):
    cursor.execute("""SELECT * FROM applicants WHERE id = (%s)""", (str(id),))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = f"User with id {id} not found")
    return {"User_detail": user}

# @app.put("/users/{id}")
# def update_user(id:int, usr:Application):
#     cursor.execute("""UPDATE applicants SET name = %s,age= %s, e_ mail= %s, p_word = %s, contact_number = %s WHERE id = %s""",
#                    (usr.name, usr.e_mail, usr.p_word, usr.contact_number,str(id))) 
#     cursor.execute("""SELECT * FROM user WHERE id = %s""", (str(id),))
#     updated_user = cursor.fetchone()
#     conn.commit()

#     if updated_user == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id {id} does not exist")
    
#     return {"data": updated_user}

@app.delete("/users/{id}")
def delete_user(id:int, response: Response):
    cursor.execute("""SELECT * FROM applicants WHERE id = %s""", (str(id),))
    deleted_user = cursor.fetchone()
    cursor.execute("""DELETE FROM applicants WHERE id = %s""", (str(id), ))
    conn.commit()
    
    if deleted_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} does not exist")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)