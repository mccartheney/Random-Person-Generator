from models import Person
from fastapi import APIRouter
from get_all_persons import get_all_persons
from person_db_generator import create_database


# create a router
router = APIRouter(prefix="/persons", tags=["persons"])

# create a Entrypoint for router using get
@router.get ("")
def return_all_people (): # create a function to return only a list of person type
    all_persons = get_all_persons()
    
    # return all persons
    return all_persons

# crete a Entrypoint to create persons
@router.get ("/create")
def create_persons () : # funtion to create persons and return them
    create_database(100) # create 100 persons
    return get_all_persons() # return them
