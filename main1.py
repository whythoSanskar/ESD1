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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechSky</title>


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
    
<div class="container-fluid">
<h1 class="text-center alert alert-danger">Python Flask CRUD Application</h1>
        <div class="row">
            <div class="col-sm-2"></div>

            <!-- content goes here -->
            <div class="col-sm-8">
<h2 >Application List <button class="btn btn-primary float-right" data-toggle="modal" data-target="#myModal">Add Student</button></h2>

{%with messages = get_flashed_messages()%}
{%if messages%}
{% for message in messages %}
<div class="alert alert-success alert-dismissable" role="alert">
    <button type="button" class="close" data-dismiss="alert" aria-label="close">
        <span aria-hidden="true">&times;</span>
    </button>
    {{message}}
</div>
{%endfor%}
{%endif%}
{%endwith%}



    <!-- Enter New Student Modal -->
    <div id="myModal" class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
   
                <div class="modal-header">
                    <h5 class="modal-title text-primary" style="align-content: center;">Please Add New Applicant</h5>    
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  

                <div class="modal-body">
                    
                    <form action="{{ url_for('insert')}}" method="POST">
                        <div class="form-group">
                          <label>Full Name</label>
                          <input type="text" name="name" class="form-control" id="exampleFormControlInput1" placeholder="Enter Full Name">
                        </div>

                        <div class="form-group">
                            <label>Email</label>
                            <input type="text" name="email" class="form-control" id="exampleFormControlInput1" placeholder="Enter Email">
                        </div>

                        <div class="form-group">
                            <label>Phone Number</label>
                            <input name="phone" type="text" class="form-control" id="exampleFormControlInput1" placeholder="Enter Phone Number">
                          </div>

                          <button type="submit" class="btn btn-primary mb-2">Save</button>
                     
                      </form>


                </div>
            </div>
        </div>

    </div>


    <!-- End of Enter New Student Modal -->




<table class="table table-hover">
    <thead>
        <tr>
            <th scope="col">S/N</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Action</th>
        </tr>
    </thead>
    <tbody>
        {% for row in students %}
        <tr>
        <td>{{row.0}}</td>
        <td>{{row.1}}</td>
        <td>{{row.2}}</td>
        <td>{{row.3}}</td>
        <td>
            <a href="/update/{{row.0}}" class="btn btn-warning btn-sm" data-toggle="modal" data-target="#modaledit{{row.0}}">Edit</a>
            <a href="/delete/{{ row.0 }}" onclick="return confirm('Are Sure Want To Deleted ?')" class="btn btn-danger btn-sm">Delete</a>

        </td>
    </tr>


        <!-- Enter New Student Modal -->
        <div id="modaledit{{row.0}}" class="modal fade" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
       
                    <div class="modal-header">
                        <h5 class="modal-title text-primary" style="align-content: center;">Update Applicant Details</h5>    
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      
    
                    <div class="modal-body">
                        
                        <form action="{{ url_for('update')}}" method="POST">
                            <input type="hidden" name="id" value="{{row.0}}">
                            <div class="form-group">
                              <label>Full Name</label>
                              <input value="{{row.1}}" type="text" name="name" class="form-control" id="exampleFormControlInput1" placeholder="Enter Full Name">
                            </div>
    
                            <div class="form-group">
                                <label>Email</label>
                                <input value="{{row.2}}" type="text" name="email" class="form-control" id="exampleFormControlInput1" placeholder="Enter Email">
                            </div>
    
                            <div class="form-group">
                                <label>Phone Number</label>
                                <input value="{{row.3}}" name="phone" type="text" class="form-control" id="exampleFormControlInput1" placeholder="Enter Phone Number">
                              </div>
    
                              <button type="submit" class="btn btn-success mb-2">Update</button>
                         
                          </form>
    
    
                    </div>
                </div>
            </div>
    
        </div>
    
    
        <!-- End of Edit Student Modal -->




        {% endfor %}
    </tbody>

</table>
            </div>
            <!-- Content ends here-->


            <div class="col-sm-2"></div>

        </div>
    </div>

 <script type="text/javascript" src="{{ url_for('static', filename='js/jquery-3.2.1.min.js') }}"></script>    
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>    
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