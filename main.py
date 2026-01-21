'''
from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World! How are you doing?'
'''
from collections import Counter
from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)
'''
@app.get('/')
async def hello_world():
    return 'Hello, World! How are you doing?'

### New Function
@app.get('/students')
async def get_students():
    return data
### End of new function

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: # Only return the student if the ID matches
      return student

    
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
                filtered_students.append(student) # add match student to the result
        return filtered_students
    return data
'''
# 1
@app.get('/students')
async def get_students_stats():
   pref = [student['pref'] for student in data]
   programme = [student['programme'] for student in data]
   return Counter(pref+programme)

# 2
@app.get('/add/{a}/{b}')
async def add(a: int,b: int):
    return (a+b)

@app.get('/subtract/{a}/{b}')
async def subtract(a: int, b: int):
    return (a-b)

@app.get('/multiply/{a}/{b}')
async def mult(a: int, b: int):
    return (a*b)

@app.get('/divide/{a}/{b}')
async def div(a: int, b:int):
    if b == 0:
        return ("Error!")
    return (a/b)



   
   
   
    








      
