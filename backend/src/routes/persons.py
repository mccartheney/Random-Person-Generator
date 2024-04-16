from models import Person
from fastapi import APIRouter
from get_all_persons import get_all_persons



# create a router
router = APIRouter(prefix="/persons", tags=["persons"])

# create a Entrypoint for router using get
@router.get ("")
def return_all_people (): # create a function to return only a list of person type
    all_persons = get_all_persons()
    
    return all_persons

@router.get ("/create")
def create_persons () :
    # do the code that create a quantity of persons
    return {"create persons"}
