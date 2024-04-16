# import Person model
from models import Person
# import json to transform dicts in json
import json
# import faker to create faker info
from faker import Faker

# init faker
faker = Faker()

# function to create database (number of persons defined when called)
def create_database (number_of_persons) :
    # array of persons
    persons = []

    # loop to create persons 
    for x in range(0,number_of_persons) :
        # create info with fake
        id = faker.uuid4()
        name = faker.name()
        age = faker.random_int(min=18, max=100)
        address = faker.address()

        # create a person model with fake info
        new_person = Person(id=id, Name=name, age=age, address=address, image="d")

        # tranform person model in dictionary (to transform in json after)
        new_person_dict = new_person.dict()

        # append person dict on person array
        persons.append(new_person_dict)

    # transform person array in json
    all_persons_json = json.dumps(persons, indent=None)

    # open database json file 
    with open ("./src/dataBase/db.json", "w") as db_file :

        # write person json data in file
        db_file.write(all_persons_json)

        # close file
        db_file.close()
