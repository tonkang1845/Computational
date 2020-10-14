from fastapi import FastAPI
from pydantic import BaseModel
#from nameko.rpc import rpc
#from nameko.standalone.rpc import ClusterRpcProxy

class Student(BaseModel):
    firstname:str
    lastname:str
    email:str

app = FastAPI() # FlaskApp()

#broker_cfg = {'AMQP_URI': "amqp://guest:guest@rabbitmq"}

@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/b2s/{text}")
def bit2int(text:str):
    s = int(text[0])
    e = int(text[1:9], 2)
    f = [ int(x) for x in text[9:]]
    x = 1 + sum([ int(f[i])*2**(-(i+1)) for i in range(len(f)) ])
    result = (-1)**s * 2**(e-127) * x 
    return {"result": result }

@app.post("/register/")
def api(student_item: Student):
    #with ClusterRpcProxy(broker_cfg) as rpc:
    #    sid =rpc.student.insert(student_item.firstname, student_item.lastname, student_item.email)
    #    rpc.enroll.insert.call_async(sid, student_item.firstname, student_item.lastname)
    #    rpc.email.send.call_async(sid, student_item.firstname, student_item.lastname, student_item.email)

    #print(sid)
    return {'results': 'registered'}
