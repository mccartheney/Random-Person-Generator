from models import Person
from typing import List
from fastapi import APIRouter

# create a router
router = APIRouter(prefix="/persons", tags=["persons"])

# create a Entrypoint for router using get
@router.get ("")
def return_all_people (): # create a function to return only a list of person type
    # do the code that return all peolpe
    return {"all people"}

@router.get ("/create")
def create_persons () :
    # do the code that create a quantity of persons
    return {"create persons"}
