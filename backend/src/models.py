from pydantic import BaseModel

class Person (BaseModel) :
    id : str
    Name : str
    age : int
    location : str
    image : str