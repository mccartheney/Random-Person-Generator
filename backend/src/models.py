from pydantic import BaseModel

class Person (BaseModel) :
    id : str
    Name : str
    age : int
    address : str
    image : str