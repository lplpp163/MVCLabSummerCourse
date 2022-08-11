import os
import json
from typing import  Union

# GLOBAL VIRIABLE
LINK = 'https://www.tiobe.com/tiobe-index/' # For Crawler
FILE_NAME = 'student.json' # for Load JSON


# PyDantic BaseModel Class
from pydantic import BaseModel
class Student(BaseModel):
    name: str
    gender: str
    birth: str
    programming_language: Union[str, None] = None

# Exception Class
class MyException(Exception):
    def __init__(self, name: str):
        self.name = name



# Web Crawler 
from pyquery import PyQuery
doc = PyQuery(url=LINK)
lans = doc.find('.td-top20').next().text().split(' ')
rates = doc.find('.td-top20').next().next().text().split(' ')
my_dict = dict(zip(lans,rates))

# FastAPI
from fastapi import FastAPI


app = FastAPI() # FastAPI Module


# Exception Handler
from fastapi.responses import JSONResponse
@app.exception_handler(MyException)
def call_exception_handler(request, exc: MyException):
    return JSONResponse (
        status_code= 420,
        content= {
            'Message' : exc.name
        }
    )

# Local data initialize
my_students = []
# Load local json file if exist
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        my_students = json.load(f)


# ROOT
@app.get('/')
def root():
    return {"message": "The TIOBE Programming Community index is an indicator of the popularity of programming languages."}

# GET RANDOM
import random
@app.get('/random')
def random_lan():
    return random.choice(list(my_dict.items()))

# GET TOP5
@app.get('/top5')
def show_top5():
    return {'This is the Top 5 TIOBE index' : dict(list(my_dict.items())[:5])}

# GET ALL
@app.get('/show-all')
def show_all():
    return {'This is the TIOBE index' : my_dict}



# POST CREATE STUDENT
from uuid import uuid4
@app.post('/add-student', response_model=Student)
def create_student(student: Student):
    student_dict = student.dict()

    #gen hex id
    student_id = uuid4().hex
    student_dict.update({"id":student_id})
    
    my_students.append(student_dict)
    
    # Save JSON File
    with open(my_file, "w") as f:
        json.dump(my_students, f, indent=4)
    return student_dict

# GET SHOW STUDENTS
@app.get('/show-students')
def show_students():
    if len(my_students):
        return {'Students' : my_students}
    else:
        raise MyException(name='No Student')


# POST UPLOAD FILE
'''
To receive uploaded files, first 'pip install python-multipart'
'''
import shutil
from fastapi import UploadFile
@app.post('/upload')
def Upload_file(file: Union[UploadFile, None] = None):
    if not file: return {"message" : "No file upload"}
    try:
        file_location = './' + file.filename
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
            file.close()
        return {"Result" : f'{file.filename} Saved'}
    except:
        raise MyException(name=f'Upload File {file.filename} Failed.')

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app= 'main:app', reload= True) # Default host = 127.0.0.1, port = 8000
